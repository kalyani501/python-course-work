Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string
s='codegnan'
s
'codegnan'
type(s)
<class 'str'>
s=''
s
''
a=10
b=20
a+b
30
a='siva'
b='kalyani'
a+b
'sivakalyani'
a=8
b='kalyani'
b*3
'kalyanikalyanikalyani'
a='-kalyani-'
a*9
'-kalyani--kalyani--kalyani--kalyani--kalyani--kalyani--kalyani--kalyani--kalyani-'
'-kalyani-*10
SyntaxError: unterminated string literal (detected at line 1)
'kalyani-'*10
'kalyani-kalyani-kalyani-kalyani-kalyani-kalyani-kalyani-kalyani-kalyani-kalyani-'
k=[1,3,5,7]
k[1]
3
k[0]
1
names='kalyani' 'siva' 'chinthamreddy'
names[:7]
'kalyani'
names[8:13]
'ivach'
names[7:10]
'siv'
names[7:11]
'siva'
names[11:24]
'chinthamreddy'
names[:-13]
'kalyanisiva'
names[-1:-12]
''
names[-1:-9]
''
'kalyani' in names
True
'kalyani' not in names
False
'z ' in names
False
'z' not in names
True
'c' in names
True
'c' not in names
False
names[-13:-1]
'chinthamredd'
names[-13:]
'chinthamreddy'
len(names)
24
ord(k)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ord(k)
TypeError: ord() expected string of length 1, but list found
ord('k')
107
ord('i')
105
ord('r')
114
chr(107)
'k'
chr(114)
'r'
chr(89)
'Y'
sorted(names)
['a', 'a', 'a', 'a', 'c', 'd', 'd', 'e', 'h', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'n', 'r', 's', 't', 'v', 'y', 'y']
max(names)
'y'
min(names)
'a'
s=sivaKalyani chinthamreddy
SyntaxError: invalid syntax
s='sivaKalyani chinthamreddy'
s.upper()
'SIVAKALYANI CHINTHAMREDDY'
s.lower()
'sivakalyani chinthamreddy'
'sivakalyani chinthamreddy's.capitalize
SyntaxError: invalid syntax
s.capitilize()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.capitilize()
AttributeError: 'str' object has no attribute 'capitilize'. Did you mean: 'capitalize'?
s.title()
'Sivakalyani Chinthamreddy'
s.captilize()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
s.capitalize()
'Sivakalyani chinthamreddy'
s.center()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.center()
TypeError: center expected at least 1 argument, got 0
s.center('*')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.center('*')
TypeError: 'str' object cannot be interpreted as an integer
s.center(30,'*')
'**sivaKalyani chinthamreddy***'
s.ljust('.')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.ljust('.')
TypeError: 'str' object cannot be interpreted as an integer
s.ljust(37,'.')
'sivaKalyani chinthamreddy............'
s.rjust(2,'_')
'sivaKalyani chinthamreddy'
s.rjust(67,'-')
'------------------------------------------sivaKalyani chinthamreddy'
'123',zfill(9)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    '123',zfill(9)
NameError: name 'zfill' is not defined
'123'.zfill(9)
'000000123'
s='chinthamreddy siva kalyani'
s.find(c)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s.find(c)
NameError: name 'c' is not defined
s.find('c')
0
s.find('h')
1
s.find('i')
2
s.rfing('i')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.rfing('i')
AttributeError: 'str' object has no attribute 'rfing'. Did you mean: 'rfind'?
>>> s.rfind('i')
25
>>> s.rfind('h')
5
>>> s.find('w')
-1
>>> s.index('c')
0
>>> s.index('k')
19
>>> s.rindex('i')
25
>>> s.index('w')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.index('w')
ValueError: substring not found
>>> s.replace('k','1')
'chinthamreddy siva 1alyani'
>>> s.replace('h','@')
'c@int@amreddy siva kalyani'
>>> s.maketrans('hik','#&*')
{104: 35, 105: 38, 107: 42}
>>> s.translate(s.maketrans('hik','#&*'))
'c#&nt#amreddy s&va *alyan&'
>>> text='hellow 🙂"
SyntaxError: unterminated string literal (detected at line 1)
>>> text="hellow 🙂"
>>> text.encode()
b'hellow \xf0\x9f\x99\x82'
>>> text.decode()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
