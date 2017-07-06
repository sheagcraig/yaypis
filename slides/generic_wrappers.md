# Generic wrappers example

- https://github.com/samgiles/slumber
- https://github.com/redodo/tortilla
- https://github.com/vintasoftware/tapioca-wrapper
- https://github.com/kadirpekel/hammock
- https://github.com/jaimegildesagredo/finch

Note:
- Tortilla bunchifies responses which is cool, but I couldn't get it to POST stuff successfully
- Finch is async, but hasn't been updated in awhile.

+++
```python
>>> import slumber
>>> auth = {'privatekey': 'PRIVATEKEY',
...		'publickey': 'PUBKEY'}
>>> api = slumber.API('https://sal.awesome.com/api/')
>>> api._store['session'].headers.update(auth)
>>> # Get all machines:
>>> # GET https://sal.awesome.com/api/machines/
>>> machines = api.machines.get()
>>> len(machines)
4723981
>>> # Get my machine
>>> # GET https://sal.awesome.com/api/machines/
>>> my_machine = api.machines('C0DEADBEEF01').get()
>>> # Create a business unit
>>> # POST https://sal.awesome.com/api/business_units/
>>> bu_data = {'name': 'taco consumption unit'}
>>> api.business_units.post(bu_data)
{'id': 13, 'name': 'taco consumption unit', 'users': []}
```
@[1]
@[2-5]
@[6-10]
@[11-13]
@[14-18]
