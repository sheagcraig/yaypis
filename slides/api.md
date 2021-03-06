# What is an **API**?

+++
# **A**pplication **P**rogramming **I**nterface

> "...a set of clearly defined methods of communication between various software components." - Wikipedia
+++
For example:
The `list` API in python

Appending an item to a list:
```python
>>> best_movies_ever = []
>>> best_movies_ever.append('Big Trouble in Little China')
>>> print(best_movies_ever)
['Big Trouble in Little China']
```

+++?code=slides/list_help.py
@[3-5]
@[96-97]
@[106-107]
@[90-91]
+++
## List methods
```shell
append insert
clear  pop
copy   remove
count  reverse
extend sort
index
```

+++
## List *magic* methods
```shell
__add__       __ge__           __iter__      __repr__
__class__     __getattribute__ __le__        __reversed__
__contains__  __getitem__      __len__       __rmul__
__delattr__   __gt__           __lt__        __setattr__
__delitem__   __hash__         __mul__       __setitem__
__dir__       __iadd__         __ne__        __sizeof__
__doc__       __imul__         __new__       __str__
__eq__        __init__         __reduce__    __subclasshook__
__format__   __init_subclass__ __reduce_ex__
```

+++
```python
>>> best_movies_ever = []
>>> best_movies_ever.append('Big Trouble in Little China')
>>> print(best_movies_ever)
['Big Trouble in Little China']
```
@[2]

+++
Meanwhile, behind the scenes...

> http://www.laurentluce.com/posts/python-list-implementation/
+++?code=slides/listobject.c
@[302-309]
@[282-300]
@[294-295]
@[42-49]
+++?image=assets/list_one_item.png&size=contain
+++?image=assets/list_4.png&size=contain
+++?image=assets/list_insert.png&size=contain
Note:
TODO Add in listobject.c's append method
TODO Do annotated code presenting to say what it's actually doing.
And for print! (show Linux print via assembler!
+++
```python
>>> best_movies_ever = []
>>> best_movies_ever.append('Big Trouble in Little China')
>>> print(best_movies_ever)
['Big Trouble in Little China']
```
@[3-4]
+++
```x86asm
push    dword len   ; Length of message (31)
push    dword msg   ; Address to beginning of string
push    dword 1     ; Output to STDOUT
mov     eax,4       ; System code for 'writing'
sub     esp,4       ; BSD needs an extra 4 bytes of stack
int     0x80        ; Interrupt to perform syscall
```

