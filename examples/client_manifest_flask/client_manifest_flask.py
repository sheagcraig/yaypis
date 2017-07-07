#!/usr/bin/env python3
"""Build client manifests when ibar data is POSTed."""


from contextlib import contextmanager
from functools import wraps
import os
import plistlib
from subprocess import check_output

from flask import Flask, Response, abort, request


__version__ = "0.3.0"
DEBUG = (True if os.getenv("CLIENT_MANIFEST_FLASK_DEBUG", "").upper() == "TRUE"
         else False)
USERNAME = os.getenv("CLIENT_MANIFEST_FLASK_USERNAME", "admin")
PASSWORD = os.getenv("CLIENT_MANIFEST_FLASK_PASSWORD", "donkeys")
DEFAULT_BUILD = os.getenv("CLIENT_MANIFEST_FLASK_DEFAULT_BUILD", "General")
DEFAULT_SITE = os.getenv("CLIENT_MANIFEST_FLASK_DEFAULT_SITE", "Winterfell")


app = Flask(__name__)


def check_credentials(user, password):
    """Return boolean whether user and password are allowed access."""
    return user == USERNAME and password == PASSWORD


def authenticate():
    """Sends a 401 response that enables basic auth."""
    return Response("Could not verify your access level for that URL.\n"
                    "You have to login with valid credentials.", 401,
                    {"WWW-Authenticate": "Basic realm='Login Required'"})


def requires_auth(f):
    """Decorator to require basic auth."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_credentials(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route("/build_manifest", methods=["GET", "POST"])
@requires_auth
def build_manifest():
    """Build a client manifest based on form data.

    Requires POST form data of ibar_data with the following keys:
        serial_number (str): The serial number of the machine.
        build (str): A build name that is present in the repo's build
            dir. Defaults to global value DEFAULT_BUILD
        site (str): A site name that is present in the repo's site dir.
            Defaults to the global value DEFAULT_SITE.
        catalog (str): The "highest" catalog level to apply. Defaults to
            "production".
    """
    form = request.form
    if not validate_form_data(form):
        abort(403)

    serial = form["serial_number"]
    build = form.get("build", DEFAULT_BUILD)
    site = form.get("site", DEFAULT_SITE)

    catalogs = get_catalogs(form.get("catalog", "production"))

    print("Creating Manifest: build: {}, site: {}, serial_number: {}".format(
        build, site, serial))

    with get_manifest(serial) as manifest:
        # Existing manifests will
        # retain contents except for catalogs, which are set to production
        # if not specified.
        manifest["catalogs"] = catalogs

        # All manifests include site_default, and then site and build if
        # available. They should always be available!
        manifest["included_manifests"] = ["site_default"]

        if site:
            manifest["included_manifests"].append(
                "included_manifests/sites/{}".format(site))
        if build:
            manifest["included_manifests"].append(
                "included_manifests/builds/{}".format(build))

    return "Manifest created."


@app.route("/testing", methods=["GET", "POST"])
@requires_auth
def enable_phase_testing():
    """Add a machine to phase testing by updating catalogs.

    Requires POST form data of ibar_data with the following keys:
        serial_number (str): The serial number of the machine to update.
        catalog (str): The "highest" catalog level to apply. Defaults to
            "phase3".
    """
    form = request.form
    if not validate_form_data(form):
        abort(403)

    catalogs = get_catalogs(form.get("catalog", "phase3"))

    print("Adding catalogs '{}' to manifest '{}'".format(
          ", ".join(catalogs), form["serial_number"]))

    with get_manifest(form["serial_number"]) as manifest:
        # Stop if there's no manifest already. This endpoint is not meant
        # to create a manifest if it doesn't already exist.
        if not manifest:
            abort(403)

        # Replace the catalogs with the one requested.
        manifest["catalogs"] = catalogs

    return "Manifest {} updated.".format(form["serial_number"])


def validate_form_data(form):
    result = True
    # Build a list of acceptable values based on what is currently
    # present.
    whitelist = get_whitelist()

    # Serial number is required.
    if not form.get("serial_number"):
        result = False

    for key in ("build", "site", "catalog"):
        val = form.get(key, None)
        # None is acceptable because there are default values for
        # everything.
        if val is not None:
            if val not in whitelist[key]:
                result = False

    return result


def get_catalogs(catalog):
    """Return a list of catalogs with <= priority to catalog."""
    catalogs = ["testing",
                "phase1",
                "phase2",
                "phase3",
                "production"]
    return catalogs[catalogs.index(catalog):]


@contextmanager
def get_manifest(serial):
    # Ensure munki repo and manifests dirs are available.
    munki_repo = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              "munki_repo")
    manifests = os.path.join(munki_repo, "manifests")
    manifest_file = os.path.join(manifests, serial)
    if not os.path.exists(manifests):
        os.makedirs(manifests)

    if not os.path.isfile(manifest_file):
        manifest = {}
        print("No manifest exists for '{}'. Creating an empty "
              "one.".format(serial))
    else:
        manifest = plistlib.readPlist(manifest_file)

    yield manifest

    plistlib.writePlist(manifest, manifest_file)
    print("Syncing {}".format(serial))


def get_whitelist():
    munki_repo = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              "munki_repo")
    whitelist = {}
    whitelist["catalog"] = os.listdir(os.path.join(munki_repo, "catalogs"))
    for val in ("build", "site"):
        whitelist[val] = os.listdir(
            os.path.join(munki_repo,
                         "manifests/included_manifests/{}s".format(val)))

    return whitelist


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=DEBUG)
