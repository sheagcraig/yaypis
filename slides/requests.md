## Python Requests
### HTTP for Humans
> Warning: Recreational use of the Python standard library for HTTP may result in dangerous side-effects, including: security vulnerabilities, verbose code, reinventing the wheel, constantly reading documentation, depression, headaches, or even death.

http://python-requests.org

+++?image=assets/use_requests.png&size=contain

+++
# Requests
```shell
pip3 install requests
```
+++
# Requests

```
>>> import requests
>>> headers = {
...		'privatekey': 'PRIVATEKEY',
...		'publickey': 'PUBLICKEY'}
>>> response = requests.get(
...		'http://sal.awesome.com/api/machines/C0DEADBEEF01',
...		verify='/path/to/sal.awesome.com.pem',
...		headers=headers)
>>> result = response.json()
```
@[1]
@[5-8]
@[9]

+++
# Curl -> Requests tool
## https://curl.trillworks.com
+++?image=assets/curl_to_requests.png&size=contain

Note:
I just copied and pasted from above example-it knows to just drop the pipe and handle the line continuations.

+++
# SSL
- Current python3 ships its own OpenSSL 1.0.2
	- Does not use macOS keychain
	- Install Certificates.command installs curated root certificates from certifi
		- https://certifi.io
- Apple's provided python 2.7.10 uses OpenSSL 0.9.8zh 14 Jan 2016 :poop:
	- Uses the Mac Security framework / keychain for verifying
	- High Sierra: python 2.7.10 ships LibreSSL 2.2.7
		- YAY TLS1.2!

+++
# Just do it
> Requests verifies SSL certificates for HTTPS requests, just like a web browser. By default, SSL verification is enabled, and Requests will throw a SSLError if it's unable to verify the certificate.

```shell
pip3 install -U certifi
```

Note:
Requests makes it super easy to do *most* SSL, and makes you work to make it less-secure.
Remember to keep certifi up to date!

+++
```
>>> import requests
>>> response = requests.get('https://pypi.org')
>>> response = requests.get('https://self_signed_cert.com')
Traceback (most recent call last):
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/urllib3/connectionpool.py", line 600, in urlopen
    chunked=chunked)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/urllib3/connectionpool.py", line 345, in _make_request
    self._validate_conn(conn)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/urllib3/connectionpool.py", line 844, in _validate_conn
    conn.connect()
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/urllib3/connection.py", line 326, in connect
    ssl_context=context)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/urllib3/util/ssl_.py", line 325, in ssl_wrap_socket
    return context.wrap_socket(sock, server_hostname=server_hostname)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 401, in wrap_socket
    _context=self, _session=session)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 808, in __init__
    self.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 1061, in do_handshake
    self._sslobj.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ssl.py", line 683, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/requests/adapters.py", line 440, in send
    timeout=timeout
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/urllib3/connectionpool.py", line 630, in urlopen
    raise SSLError(e)
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/requests/api.py", line 72, in get
    return request('get', url, params=params, **kwargs)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/requests/api.py", line 58, in request
    return session.request(method=method, url=url, **kwargs)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/requests/sessions.py", line 502, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/requests/sessions.py", line 612, in send
    r = adapter.send(request, **kwargs)
  File "/Users/shcrai/Developer/yaypis/examples/giphy/venv/lib/python3.6/site-packages/requests/adapters.py", line 514, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)
```
@[2]
@[3]
@[23]
+++
```
>>> import requests
>>> my_self_signed_cert = '/path/to/self_signed_cert.com.pem'
>>> response = requests.get(
...		'https://self_signed_cert.com',
...		verify=my_self_signed_cert)
>>> I_am_a_bad_person = requests.get(
...		'https://self_signed_cert.com',
...		verify=False)
```
@[2-5]
@[6-8]

+++
# Sessions

Note:
Sessions allow you to specify things like SSL verify, cookies, headers, and use TCP connection pooling.

```
>>> import requests
>>> sesh = requests.Session()
>>> sesh.headers.update({'Accept': 'application/json'})
>>> sesh.verify = '/path/to/cert.pem'
>>> sesh.auth = ('rasputin', 'correct horse battery staple')
>>> sesh.get('https://breakdance.com')
<Response [200]>
>>> sesh.get('https://breakdance.com/twistoflex')
<Response [200]>
>>> response = sesh.get('https://breakdance.com/headspin')
>>> ('Accept' in sesh.headers and sesh.headers['Accept']' == application/json')
True
```
@[2-5]
@[10]
@[11-12]

+++
# Authentication with Requests
http://docs.python-requests.org/en/master/user/authentication/

```
>>> import requests
>>> requests.get(
...		'https://api.sparklemotion.com/user',
...		auth=SOME_KIND_OF_AUTH)
<Response [200]>
```
+++
# Authentication with Requests
## Basic
```
>>> import requests
>>> requests.get(
...		'https://api.sparklemotion.com/user',
...		auth=('emilio', '2L3374u!'))
<Response [200]>
```
@[4]

Note:
Basic auth can be just a 2-tuple of username and password passed to the auth parameter.

+++
# Authentication with Requests
## Token Authentication

+++
# Authentication with Requests
## OAUTH

Note:
TODO switch to using requests-oauthlib (oauth2, plugs into requests)
