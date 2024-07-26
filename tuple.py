Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(21,36,81,45)
>>> tup
(21, 36, 81, 45)
>>> tup[1]
36
>>> tup[1:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> tup[1:]
(36, 81, 45)
>>> tup(1)=6
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> tup[1]=6
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tup[1]=6
TypeError: 'tuple' object does not support item assignment
>>> tup.index(36)
1
>>> tup.count()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tup.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> tup.count(2)
0
>>> values=(1,5,6,8,1,2)
>>> values
(1, 5, 6, 8, 1, 2)
>>> values.count(1)
2
