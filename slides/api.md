# What is an <span style='color: #3DE9FE'>API</span>?

+++
# <span style='color: #3DE9FE'>A</span>pplication <span style='color: #3DE9FE'>P</span>rogramming <span style='color: #3DE9FE'>I</span>nterface

> "...a set of clearly defined methods of communication between various software components." - Wikipedia
+++
For example:
The `list` API in python

+++?code=list_help.py
@[3-5]
@[90-91]

Note:
Do the code presenting here

+++
Appending an item to a list:
```
>>> best_movies_ever = []
>>> best_movies_ever.append('Big Trouble in Little China')
>>> print(best_movies_ever)
['Big Trouble in Little China']
```
+++
Meanwhile, behind the scenes:
Note:
TODO Add in listobject.c's append method
TODO Do annotated code presenting to say what it's actually doing.
+++

# CRUD
Note:
TODO The major functions needed for manipulating data in persistent storage (i.e. a database)
TODO Other acronyms are BREAD (Browse, read, edit, add delete) CRAP (Create, retrieve, alter, purge)
TODO Most of what we're interested in is data from a database, potentially as manipulated by a web app.
+++
# Requests
Note:
I guess my point here was to go over what a request is
+++
# Responses
Note:
and what a response is (what it looks like?)
+++
# Status codes
Note:
Go over standard response codes
