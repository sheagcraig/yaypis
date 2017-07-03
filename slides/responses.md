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
>>> computers = jss.Computer()
>>> good_name = lambda e: re.match(
...		pattern, e.find('general').find('name').text
>>> misnamed = [c for c in computers if not good_name(c)]
```
@[1-2]
@[3]
@[4-5]
@[6]

Note:
Result is a LIST of COMPUTER objects that you can then operate on.

+++
## Comparing Two Groups

```python
>>> misnamed = {c for c in computers if not good_name(c)}
>>> missing = {c for c in computers if no_checkins(c, days=30)}
>>> misnamed_and_missing = misnamed.intersection(missing)
>>> misnamed_but_not_missing = misnamed - missing
>>> # or `misnamed.difference(missing)`

Note:
These are sets of Computer objects, essentially Elements

+++
## Printing XML

```python
>>> print(ET.tostring(computers[0]))
<computer><computer><general><id>461</id><name>FS-CRAIGS</name><mac_address>3C:15:C2:DE:6F:26</mac_address><alt_mac_address>72:00:04:07:A4:C0</alt_mac_address><ip_address>10.17.8.38</ip_address><serial_number>C0DEADBEEF01</serial_number><udid>F79E84CB-3227-5C69-F32G-6C45C2E77DF5</udid><jamf_version>9.81</jamf_version><platform>Mac</platform><barcode_1 /><barcode_2 /><asset_tag /><remote_management><managed>true</managed><management_username>casper_admin</management_username></remote_management><mdm_capable>true</mdm_capable><mdm_capable_users><mdm_capable_user>scraig</mdm_capable_user></mdm_capable_users><report_date>2015-10-06 11:57:03</report_date><report_date_epoch>1444147023495</report_date_epoch><report_date_utc>2015-10-06T11:57:03.495-0400</report_date_utc><last_contact_time>2015-10-07 08:48:27</last_contact_time><last_contact_time_epoch>1444222107871</last_contact_time_epoch><last_contact_time_utc>2015-10-07T08:48:27.871-0400</last_contact_time_utc><initial_entry_date>2014-07-01</initial_entry_date><initial_entry_date_epoch>1404241243921</initial_entry_date_epoch><initial_entry_date_utc>2014-07-01T15:00:43.921-0400</initial_entry_date_utc><last_cloud_backup_date_epoch>0</last_cloud_backup_date_epoch><last_cloud_backup_date_utc /><distribution_point /><sus /><netboot_server>US Services Netboot Server</netboot_server><site><id>-1</id><name>None</name></site><itunes_store_account_is_active>true</itunes_store_account_is_active></general><hardware><make>Apple</make><model>15-inch Retina MacBook Pro (Late 2013)</model><model_identifier>MacBookPro11,2</model_identifier><os_name>Mac OS X</os_name><os_version>10.11.0</os_version><os_build>15A284</os_build><active_directory_status>school.da.org</active_directory_status><service_pack /><processor_type>Intel Core i7</processor_type><processor_architecture>i386</processor_architecture><processor_speed>2000</processor_speed><processor_speed_mhz>2000</processor_speed_mhz><number_processors>4</number_processors><total_ram>8192</total_ram><total_ram_mb>8192</total_ram_mb><boot_rom>MBP112.0138.B15</boot_rom><bus_speed>0</bus_speed><bus_speed_mhz>0</bus_speed_mhz><battery_capacity>96</battery_capacity><cache_size>6144</cache_size><cache_size_kb>6144</cache_size_kb><available_ram_slots>0</available_ram_slots><optical_drive /><nic_speed>n/a</nic_speed><smc_version>2.18f15</smc_version><storage><device><disk>disk0</disk><model>APPLE SSD SM0256F</model><revision>UXM2JA1Q</revision><serial_number>S1K4NYBF519218</serial_number><size>257024</size><drive_capacity_mb>257024</drive_capacity_mb><connection_type>NO</connection_type><smart_status>Verified</smart_status><partition><name>Macintosh HD (Boot Partition)</name><size>238208</size><type>boot</type><partition_capacity_mb>238208</partition_capacity_mb><percentage_full>82</percentage_full><filevault_status>Encrypted</filevault_status><filevault_percent>100</filevault_percent><filevault2_status>Encrypted</filevault2_status><filevault2_percent>100</filevault2_percent><lvgUUID>3410FE0F-F53F-4FE2-A970-3D2FF3584A4E</lvgUUID><lvUUID>2222C7BB-2B74-46F0-B317-3A6A145FA8C5</lvUUID><pvUUID>F0F62D12-B315-40E5-88AF-339352762C64</pvUUID></partition></device></storage></hardware></computer></computer>
```

+++
## **Pretty** Printing XML

```
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
            if kid.tag == "data":
                kid.text = "*DATA*"
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
```

+++
## **Pretty** Printing XML

```python
>>> import copy
>>> pretty_data = copy.deepcopy(computer)
>>> indent_xml(pretty_data)
>>> print(ElementTree.tostring(pretty_data, encoding='UTF-8'))

+++
## lxml
```python
>>> from lxml import etree
>>> response = get_computer_xml_with_requests()
>>> computer = etree.fromstring(response.content)
>>> print(etree.tostring(computer, pretty_print=True))
```

+++?code=slides/fs-craigs.xml

TODO:
tree-printing/exploration
xml_tree.md

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
