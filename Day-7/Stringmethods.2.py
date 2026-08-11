Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sring(trimming methods)
s= '             siva          kalyani        '
s.strip()
'siva          kalyani'
s.lstrip()
'siva          kalyani        '
s.rstip()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.rstip()
AttributeError: 'str' object has no attribute 'rstip'. Did you mean: 'rstrip'?
s.rstrip()
'             siva          kalyani'
s.replace(' ','')
'sivakalyani'
#string partions
s='kalyani chinthamreddy'
s.split()
['kalyani', 'chinthamreddy']
s='kalyani-chinthamreddy'
s.split('-')
['kalyani', 'chinthamreddy']
s.split('-',2)
['kalyani', 'chinthamreddy']
s='kalyani priyanka sadhana'
s.rsplit(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.rsplit(2)
TypeError: must be str or None, not int
s.rsplit('',2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.rsplit('',2)
ValueError: empty separator
rs='kalyani-priyanka-sadhana'
rs.rsplit('-',2)
['kalyani', 'priyanka', 'sadhana']
rs='kalyani-priyanka-sadhana-siva-pavani'
rs.rsplit('-',2)
['kalyani-priyanka-sadhana', 'siva', 'pavani']
rs.lsplit('-',3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    rs.lsplit('-',3)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
s='''kalyani
pavani
priyanka
siva
kavya''''
SyntaxError: unterminated string literal (detected at line 5)
s='''kalyani
python
java
siva'''
s
'kalyani\npython\njava\nsiva'
s.splitlines()
['kalyani', 'python', 'java', 'siva']
s=[1,2,3,4,5]
'-'.join()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    '-'.join()
TypeError: str.join() takes exactly one argument (0 given)
'-'.join(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    '-'.join(s)
TypeError: sequence item 0: expected str instance, int found
s='kalyani siva chinthamreddy'
'%'.join(s)
'k%a%l%y%a%n%i% %s%i%v%a% %c%h%i%n%t%h%a%m%r%e%d%d%y'
a='python full stavck'
a.startswith('py')
True
a.startswith('za')
False
a.endswith('ck')
True
a.endswith('ty')
False
s='kalyani76'
s.isalpha()
False
s='ujytgg'
s.isalpha
<built-in method isalpha of str object at 0x000002491EA4FC00>
s.isalpha()
True
n=12345
n.isnum()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    n.isnum()
AttributeError: 'int' object has no attribute 'isnum'
s='python with dsa'
s.isupper()
False
s.islower()
True
s='Python full satck with ai'
s.isupper()
False
s='Siva Kalyani Chinthamreddy'
s.isupper()
False
s='KALYANI'
s.isupper()
True
s='kalyani23'
s.isallnum()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.isallnum()
AttributeError: 'str' object has no attribute 'isallnum'. Did you mean: 'isalnum'?
>>> s.isalnum()
True
>>> s=j&89hr
SyntaxError: invalid decimal literal
>>> s='j&89hr'
>>> s.isalnum()
False
>>> s='poiuytrertyuio'
>>> s.isalnum()
True
>>> s='56789'
>>> s.isalnum()
True
>>> s='    '
>>> s.isspace()
True
>>> s=' n    '
>>> s.isspace()
False
>>> s='Hlo Wrold'
>>> s.istitle()
True
>>> s='FGHJK'
>>> s.istitle()
False
>>> s='kalyani_89'
>>> s.isidentifier()
True
>>> s="2h_l'
SyntaxError: unterminated string literal (detected at line 1)
>>> s='@if_p'
>>> s.isidentifier()
False
>>> '0909'.isnumeric()
True
>>> '6'.isdigit()
True
