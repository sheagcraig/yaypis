# Copyright (C) 2014-2017 Shea G Craig
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
"""pretty_element.py

Pretty-printing xml.etree.ElementTree.Element subclass
"""


import copy
import re
from xml.etree import ElementTree

import tools


_DUNDER_PATTERN = re.compile(r'__[a-zA-Z]+__')


class PrettyElement(ElementTree.Element):
    """Pretty printing element subclass

    Element subclasses xml.etree.ElementTree.Element to pretty print.
    """

    def __init__(self, tag, attrib={}, **extra):
        if isinstance(tag, ElementTree.Element):
            super(PrettyElement, self).__init__(tag.tag, tag.attrib, **extra)
            self.text = tag.text
            self.tail = tag.tail
            self._children = [PrettyElement(child) for child in tag]
        else:
            super(PrettyElement, self).__init__(tag, attrib, **extra)

    # Replace standard Element.__str__ with our
    # pretty-printing one.
    __str__ = tools.element_str

    def __getattr__(self, name):
        if re.match(_DUNDER_PATTERN, name):
            return super(PrettyElement, self).__getattr__(name)
        result = self.find(name)
        if result is not None:
            return result
        else:
            raise AttributeError(
                'There is no element with the tag "{}"'.format(name))

    def makeelement(self, tag, attrib):
        """Return a PrettyElement with tag and attrib."""
        # We have to override Element's makeelement, which uses the
        # class' __init__. Since python-jss objects override this and
        # repurpose it, instantiating a sub element with
        # ElementTree.SubElement or copy will fail.

        # This situation will be resolved when JSSObject stops
        # subclassing Element.
        return PrettyElement(tag, attrib)

    def append(self, item):
        self._children.append(self._convert(item))

    def insert(self, index, item):
        self._children.insert(index, self._convert(item))

    def extend(self, items):
        self._children.extend(self._convert(item) for item in items)

    def _convert(self, item):
        """If item is not a PrettyElement, make it one"""
        return item if isinstance(item, PrettyElement) else PrettyElement(item)


def indent_xml(elem, level=0, more_sibs=False):
    """Indent an xml element object to prepare for pretty printing.

    To avoid changing the contents of the original Element, it is
    recommended that a copy is made to send to this function.

    Args:
        elem: Element to indent.
        level: Int indent level (default is 0)
        more_sibs: Bool, whether to anticipate further siblings.
    """
    i = "\n"
    pad = "    "
    if level:
        i += (level - 1) * pad
    num_kids = len(elem)
    if num_kids:
        if not elem.text or not elem.text.strip():
            elem.text = i + pad
            if level:
                elem.text += pad
        count = 0
        for kid in elem:
            indent_xml(kid, level + 1, count < num_kids - 1)
            count += 1
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
            if more_sibs:
                elem.tail += pad
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
            if more_sibs:
                elem.tail += pad


def element_str(elem):
    """Return a string with indented XML data."""
    # deepcopy so we don't mess with the valid XML.
    pretty_data = copy.deepcopy(elem)
    indent_xml(pretty_data)
    return ElementTree.tostring(pretty_data, encoding='UTF-8')

