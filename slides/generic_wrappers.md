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
```
sal = slumber.wrap('https://sal.awesome.com/api/')
sal.machines('C0DEADBEEF01').get()
```
Every attribute and method call represents a part of the URL

```
sal         -> https://sal.awesome.com/api/
.machines   -> /machines
(S/N)       -> /C0DEADBEEF01
.get() 		-> /
Final URL   -> https://sal.awesome.com/api/machines/C0DEADBEEF01/
```

+++
```python
>>> import slumber
>>> auth = {'privatekey': 'PRIVATEKEY',
...		'publickey': 'PUBKEY'}
>>> sal = slumber.API('https://sal.awesome.com/api/')
>>> sal._store['session'].headers.update(auth)
>>> # Get all machines:
>>> # GET https://sal.awesome.com/api/machines/
>>> machines = sal.machines.get()
>>> len(machines)
4723981
>>> # Get my machine
>>> # GET https://sal.awesome.com/api/machines/C0DEADBEEF01/
>>> my_machine = sal.machines('C0DEADBEEF01').get()
>>> # Create a business unit
>>> # POST https://sal.awesome.com/api/business_units/
>>> bu_data = {'name': 'taco consumption unit'}
>>> sal.business_units.post(bu_data)
{'id': 13, 'name': 'taco consumption unit', 'users': []}
```
@[1]
@[2-5]
@[6-10]
@[11-13]
@[14-18]
