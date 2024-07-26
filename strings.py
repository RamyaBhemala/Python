Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name='ramya'
>>> name
'ramya'
>>> name[0]
'r'
>>> name[1]='s'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name[1]='s'
TypeError: 'str' object does not support item assignment
>>> name[-1]
'a'
>>> name[1:]
'amya'
>>> name[:3]
'ram'
>>> name[0:3]
'ram'
>>> 'my'+name
'myramya'
>>> len(name)
5
