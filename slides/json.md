# JSON

```python
>>> import json
>>> response = get_computer_json()
>>> computer = response.json()
>>> computer['general']['name']
'FS-CRAIGS'
>>> type(computer)
<class 'dict'>
```

Note:
JSON 'vanishes' once parsed. It's just nested dictionaries and lists at that point.
(and ints and strings)

+++
# Parsing JSON

```python
>>> import json
>>> response = get_some_json()
>>> taco_tweets = json.loads(response.text)
```
Note:
Json not afraid of Unicode

+++
# Pretty Printing JSON

```python
>>> print(json.dumps(computer, indent=4))
{
    "general": {
        "name": "FS-CRAIGS",
        "id": 42,
        "mac_address": "3C:15:C2:DE:6F:26"
	...
}
```

Note:
json.dumps just takes native python types in! Not a "special" json type.
