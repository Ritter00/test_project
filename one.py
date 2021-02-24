Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:08:11) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x, y):
	return x + y

>>> add(5, 6)
11
>>> help(add)
Help on function add in module __main__:

add(x, y)

>>> 
================================ RESTART: Shell ================================
>>> import math
>>> sqrt(256)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sqrt(256)
NameError: name 'sqrt' is not defined
>>> import sqrt from math
SyntaxError: invalid syntax
>>> math.sqrt(256)
16.0
>>> math.sqrt(256)-100
-84.0
>>> 