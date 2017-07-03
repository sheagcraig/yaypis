# XML

```xml
<tag attribute='attr value'>text</tag>
```

```xml
<parent>
	<child></child>
</parent>
```

+++

# ElementTree & lxml

```
>>> from xml.etree import ElementTree as ET
>>> response = get_computer_xml_with_requests()
>>> computer = ET.fromstring(response.content)
```
@[1]
@[2-3]

+++?code=slides/fs-craigs.xml

+++
```
>>> # Elements are lists
>>> for child in computer:
...		print(child.tag)
General
Hardware
Location
Purchasing
```

+++

```python
>>> # Elements contain text
>>> computer[0][0][1].text
'fs-craigs'
>>> # Instead of using list indexing, we can find
>>> general = computer.find('general')
>>> for element in general:
...		text = element.text or ''
...		print('{}:\t{}'.format(element.tag, text)
id: 461
name: FS-CRAIGS
mac_address: 3C:15:C2:DE:6F:26
alt_mac_address: 72:00:04:07:A4:C0
ip_address: 10.17.8.38
serial_number: C0DEADBEEF01
udid: E79E84CB-3227-5C69-F32G-6C45C2E77DF5
```
@[1-3]
@[4-5]
@[6-8]
@[9-15]

+++
## Relating Items
```
>>> import re
>>> pattern = r'FS[A-Z]+'
>>> all_computers = jss.Computer()
>>> good_name = lambda e: re.match(
...		pattern, e.find('general').find('name').text
>>> misnamed = [c for c in all_computers if not good_name(c)]
```
@[1-2]
@[3]
@[4-5]
@[6]

Note:
Result is a LIST of COMPUTER objects that you can then operate on.

+++

Note:
pretty printing methods with raw python and lxml
tree-printing/exploration

+++
# JSON
Note:
pretty printing, tree-printing/exploration

---
# Common data handling tasks
+++
# Set arithmetic
+++
# Relating data
+++
# ML
+++
# Visualization
+++
# Automation
---
# HTML
