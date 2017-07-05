#!/usr/bin/python


# Copyright (C) 2016 Shea G Craig <shea.craig@sas.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Python module to perform Google Custom Search Engine Image Searches"""


import requests


# pylint: disable=too-few-public-methods
class ImageSize(object):
    """Defines acceptable size parameters."""
    huge = "huge"
    icon = "icon"
    large = "large"
    medium = "medium"
    small = "small"
    xlarge = "xlarge"
    xxlarge = "xxlarge"


class ImageType(object):
    """Defines acceptable image type parameters."""
    clipart = "clipart"
    face = "face"
    lineart = "lineart"
    news = "news"
    photo = "photo"


class SafeMode(object):
    """Defines acceptable image type parameters."""
    high = "high"
    medium = "medium "
    off = "off"

# pylint: enable=too-few-public-methods


class GoogleImageSearch(object):
    """Class for searching Google Images.

    The proper image search API has been deprecated.

    This method makes use of the Custom Search Engine feature at the
    free tier to make up to 100 searches per day. Please see the
    documentation provided with this code to set up a custom search
    engine.
    """
    base_url = "https://www.googleapis.com/customsearch/v1"

    def __init__(self, cx, key):
        self.cx = cx  # pylint: disable=invalid-name
        self.key = key
        self.pages = []
        self.page_index = 1
        self.query = None
        self.parameters = {}

    def search(self, query, **kwargs):
        """Perform an image search with optional search arguments.

        A maximum of 10 results are returned at a time. The search
        results are cached in the pages property until a new search
        is performed.

        Args:
            query (str): Search terms to query.
            kwargs: Optional search parameters accepted by the CSE.
                Python classes / faux enums are provided for supported
                values:
                    imageSize (ImageSize): Filter by image size.
                    imageType (ImageType): Filter by image content.
                    safe (SafeMode): Search safety level.

        Returns:
            Json response as native python lists / dicts.
        """
        self.pages = []
        self.page_index = 1
        self.query = query
        self.parameters = kwargs
        self._search()

    def _search(self):
        """Perform an image search with optional search arguments.

        A maximum of 10 results are returned at a time. The search
        results are cached in the pages property until a new search
        is performed.

        Args:
            query (str): Search terms to query.
            kwargs: Optional search parameters accepted by the CSE.
                Python classes / faux enums are provided for supported
                values:
                    imageSize (ImageSize): Filter by image size.
                    imageType (ImageType): Filter by image content.
                    safe (SafeMode): Search safety level.
        """
        # Parameters documentation:
        # https://developers.google.com/custom-search/json-api/v1/reference/cse/list#parameters
        # "num" is number of results to get per request, 1-10 inclusive.
        # "searchType" is mandatory to constrain results to images.
        # "start" is the result pager.
        request_parameters = {"cx": self.cx, "key": self.key, "q": self.query,
                              "searchType": "image", "num": 10, "start":
                              self.page_index}
        for param in self.parameters:
            request_parameters[param] = self.parameters[param]
        response = requests.get(self.base_url, request_parameters)
        self.pages.append(response.json())

    def next(self):
        """Request the next 10 image search results from last search."""
        if not self.query:
            return
        self.page_index += 10
        self._search()

    def links(self):
        """Return the links for all found images."""
        return [item["link"] for response in self.pages for item in
                response.get("items", [])]

    def items(self):
        """Return all data for all found images."""
        return [item for response in self.pages for item in response["items"]]


def main():
    """Run tests."""
    pass


if __name__ == "__main__":
    main()
