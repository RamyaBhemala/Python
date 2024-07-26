Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={4,8,6,25,3}
>>> s
{3, 4, 6, 8, 25}
>>> s={5,5,5,2,6,8}
>>> s
{8, 2, 5, 6}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> s.add(2)
>>> s
{8, 2, 5, 6}
>>> s.add(10)
>>> s
{2, 5, 6, 8, 10}
>>> s.pop(5)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.pop(5)
TypeError: set.pop() takes no arguments (1 given)
>>> s.pop(1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.pop(1)
TypeError: set.pop() takes no arguments (1 given)
>>> s.pop()
2
