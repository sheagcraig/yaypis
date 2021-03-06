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
```

Note:
These are sets of Computer objects, essentially Elements

+++
## Printing XML

```python
>>> print(ET.tostring(computers[0]))
<computer><computer><general><id>461</id><name>FS-CRAIGS</n
ame><mac_address>3C:15:C2:DE:6F:26</mac_address><alt_mac_add
ress>72:00:04:07:A4:C0</alt_mac_address><ip_address>10.17.8.
38</ip_address><serial_number>C0DEADBEEF01</serial_number><u
did>F79E84CB-3227-5C69-F32G-6C45C2E77DF5</udid><jamf_version
>9.81</jamf_version><platform>Mac</platform><barcode_1 /><ba
rcode_2 /><asset_tag /><remote_management><managed>true</man
aged><management_username>casper_admin</management_username>
6<F3</remote_management><mdm_capable>true</mdm_capable><mdm_
capable_users><mdm_capable_user>scraig</mdm_capable_user></m
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
```

+++
## lxml
```python
>>> from lxml import etree
>>> response = get_computer_xml_with_requests()
>>> computer = etree.fromstring(response.content)
>>> print(etree.tostring(computer, pretty_print=True))
```

+++?code=slides/fs-craigs.xml

Note:
Why do we care? Because we don't know the structure of all of the data we
intend to work with. Need to be able to explore.

+++
## Exploring XML Data

```python
def tree(self, element, level=0):
	results = []
	space = ' '
	indent_size = 4
	for child in element:
		entry = space * indent_size * level + child.tag
		if entry not in results:
			results.append(entry)
			if len(child):
				results.extend(self._get_tags(child, level + 1))

	return results
```

+++
```python
>>> print(tree(computer))
```

+++

```
general
    id
    name
    mac_address
    alt_mac_address
    ip_address
    last_reported_ip
    serial_number
    udid
    jamf_version
    platform
    barcode_1
    barcode_2
    asset_tag
    remote_management
        managed
        management_username
        management_password_sha256
    mdm_capable
    mdm_capable_users
    report_date
    report_date_epoch
    report_date_utc
    last_contact_time
    last_contact_time_epoch
    last_contact_time_utc
    initial_entry_date
    initial_entry_date_epoch
    initial_entry_date_utc
    last_cloud_backup_date_epoch
    last_cloud_backup_date_utc
    last_enrolled_date_epoch
    last_enrolled_date_utc
    distribution_point
    sus
    netboot_server
    site
        id
        name
    itunes_store_account_is_active
location
    username
    realname
    real_name
    email_address
    position
    phone
    phone_number
    department
    building
    room
purchasing
    is_purchased
    is_leased
    po_number
    vendor
    applecare_id
    purchase_price
    purchasing_account
    po_date
    po_date_epoch
    po_date_utc
    warranty_expires
    warranty_expires_epoch
    warranty_expires_utc
    lease_expires
    lease_expires_epoch
    lease_expires_utc
    life_expectancy
    purchasing_contact
    os_applecare_id
    os_maintenance_expires
    attachments
peripherals
    size
hardware
    make
    model
    model_identifier
    os_name
    os_version
    os_build
    master_password_set
    active_directory_status
    service_pack
    processor_type
    processor_architecture
    processor_speed
    processor_speed_mhz
    number_processors
    number_cores
    total_ram
    total_ram_mb
    boot_rom
    bus_speed
    bus_speed_mhz
    battery_capacity
    cache_size
    cache_size_kb
    available_ram_slots
    optical_drive
    nic_speed
    smc_version
    ble_capable
    sip_status
    gatekeeper_status
    institutional_recovery_key
    disk_encryption_configuration
    filevault2_users
    storage
        device
            disk
            model
            revision
            serial_number
            size
            drive_capacity_mb
            connection_type
            smart_status
            partition
                name
                size
                type
                partition_capacity_mb
                percentage_full
                filevault_status
                filevault_percent
                filevault2_status
                filevault2_percent
                boot_drive_available_mb
                lvgUUID
                lvUUID
                pvUUID
    mapped_printers
        printer
            name
            uri
            type
            location
certificates
    certificate
        common_name
        identity
        expires_utc
        expires_epoch
        name
software
    unix_executables
    licensed_software
    installed_by_casper
        package
    installed_by_installer_swu
        package
    cached_by_casper
    available_software_updates
    available_updates
    running_services
        name
    applications
        size
        application
            name
            path
            version
    fonts
        size
    plugins
        size
extension_attributes
    extension_attribute
        id
        name
        type
        value
groups_accounts
    computer_group_memberships
        group
    local_accounts
        user
            name
            realname
            uid
            home
            home_size
            home_size_mb
            administrator
            filevault_enabled
iphones
    size
configuration_profiles
    size
    configuration_profile
        id
        name
        uuid
        is_removable
```

+++
```
>>> computer.find('general').find('name').text
'FS-CRAIGS'
>>> computer[1].find('model').text
'Apple IIGS'
>>> len(computer.find('hardware').find('storage'))
1
```

+++?code=examples/casperstuff/pretty_element.py
@[50-58]

Note:
This works by converting all Element objects it takes in into PrettyElements

+++
```
>>> computer.general.name.text
'FS-CRAIGS'
>>> computer.hardware.model.text
'Apple IIGS'
>>> len(computer.hardware.storage)
1
```

