Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data={1:'ramya',2:'swathi',3:'namitha'}
>>> data
{1: 'ramya', 2: 'swathi', 3: 'namitha'}
>>> dat[3]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dat[3]
NameError: name 'dat' is not defined. Did you mean: 'data'?
>>> data[3]
'namitha'
>>> data[1:]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[1:]
KeyError: slice(1, None, None)
>>> data.get(1)
'ramya'
>>> data.pop(1)
'ramya'
>>> data
{2: 'swathi', 3: 'namitha'}

