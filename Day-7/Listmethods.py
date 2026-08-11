Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list
l=[]
type(l)
<class 'list'>
l=list()
type(l)
<class 'list'>
l=[1,'python',8.9,{8,9},9+9j]
l
[1, 'python', 8.9, {8, 9}, (9+9j)]
l=[2,4,5,6]
l
[2, 4, 5, 6]
l=[9,9,9,9]
l
[9, 9, 9, 9]
l=[1,'python',8.9,{8,9},9+9j,True,{k:9}]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l=[1,'python',8.9,{8,9},9+9j,True,{k:9}]
NameError: name 'k' is not defined
l=[1,'python',8.9,{8,9},9+9j,True,{'k':9}]
l
[1, 'python', 8.9, {8, 9}, (9+9j), True, {'k': 9}]
#list operations
a=[1,2,3]
b=[5,8,9]
c=a+b
c
[1, 2, 3, 5, 8, 9]
a*9
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
s=[90,89,99,67,87]
s[0]
90
s[5]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s[5]
IndexError: list index out of range
s[4]
87
s[-1]
87
s[:2]
[90, 89]
s[1:4]
[89, 99, 67]
s[:-4]
[90]
s[-1:-4]
[]
s[-1:-4:1]
[]
s[-1:-4:-1]
[87, 67, 99]
s[1:4:2]
[89, 67]
s[-1:-5:-3]
[87, 89]
90 in s
True
90 not in s
False
89 in s
True
100 not in s
True
a=[87,90,98,23,45,67]
a
[87, 90, 98, 23, 45, 67]
max(a)
98
min(a)
23
sorted(a)
[23, 45, 67, 87, 90, 98]
a.sorted()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
sorted(a)
[23, 45, 67, 87, 90, 98]
len(a)
6
a=[123,87,90,66,54,890,89]
a
[123, 87, 90, 66, 54, 890, 89]
id(a)
1324547306560
a[0]
123
a[0]=23
a
[23, 87, 90, 66, 54, 890, 89]
a.append(90)
a
[23, 87, 90, 66, 54, 890, 89, 90]
a.append(89)
a
[23, 87, 90, 66, 54, 890, 89, 90, 89]
a.insert(1,99)
a
[23, 99, 87, 90, 66, 54, 890, 89, 90, 89]
a.insert(-1,89)
a
[23, 99, 87, 90, 66, 54, 890, 89, 90, 89, 89]
a.extend([1,2,3,4])
a
[23, 99, 87, 90, 66, 54, 890, 89, 90, 89, 89, 1, 2, 3, 4]
id(a)
1324547306560
a.pop()
4
a
[23, 99, 87, 90, 66, 54, 890, 89, 90, 89, 89, 1, 2, 3]
a.pop(0)
23
a
[99, 87, 90, 66, 54, 890, 89, 90, 89, 89, 1, 2, 3]
a.remove(90)
a
[99, 87, 66, 54, 890, 89, 90, 89, 89, 1, 2, 3]
a.remove(66)
a
[99, 87, 54, 890, 89, 90, 89, 89, 1, 2, 3]
del a[0]
a
[87, 54, 890, 89, 90, 89, 89, 1, 2, 3]
del a[0:2]
a
[890, 89, 90, 89, 89, 1, 2, 3]
a.clear()
a
[]
a=[1,2,3,4,5,67,90]
>>> a.index(1)
0
>>> a.index(90)
6
>>> a.count(1)
1
>>> a=b
>>> b=a.copy()
>>> b.append(23)
>>> a
[5, 8, 9]
>>> b
[5, 8, 9, 23]
>>> a=[1,9,[],False,{}]
>>> any(a)
True
>>> all(a)
False
>>> sum(a)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    sum(a)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> a=[9,0,56,89,9]
>>> sum(a)
163
>>> a.reverse()
>>> a
[9, 89, 56, 0, 9]
>>> a=[1,2,3,4,5]
>>> sorted(a)
[1, 2, 3, 4, 5]
>>> sort(a)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    sort(a)
NameError: name 'sort' is not defined
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
