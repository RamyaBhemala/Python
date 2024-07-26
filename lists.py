Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=[1,52,95,36,74]
num
[1, 52, 95, 36, 74]
num[0]
1
num[2]=80
num
[1, 52, 80, 36, 74]
num[2:]
[80, 36, 74]
names=['ramya','swathi','namitha']
nmaes
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    nmaes
NameError: name 'nmaes' is not defined. Did you mean: 'names'?
names
['ramya', 'swathi', 'namitha']
values=[92,'ramya',5.66]
values
[92, 'ramya', 5.66]
ouput=[names,values]
output
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    output
NameError: name 'output' is not defined. Did you mean: 'ouput'?
>>> ouput
[['ramya', 'swathi', 'namitha'], [92, 'ramya', 5.66]]
>>> num.append(66)
>>> num
[1, 52, 80, 36, 74, 66]
>>> num.insert(3,10)
>>> num
[1, 52, 80, 10, 36, 74, 66]
>>> num.remove(36)
>>> num
[1, 52, 80, 10, 74, 66]
>>> del nums()
SyntaxError: cannot delete function call
>>> del num()
SyntaxError: cannot delete function call
>>> del num[2:]
>>> num
[1, 52]
>>> min(num)
1
>>> max(num)
52
>>> sort(values)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sort(values)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> values.sort()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    values.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> sort.num()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sort.num()
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> num.sort()
>>> num
[1, 52]
>>> sum(num)
53
