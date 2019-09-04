Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.ceil(2.56)
3
>>> math.floor(3.85)
3
>>> math.fabs(-14.63)
14.63
>>> math.gcd(5/25)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    math.gcd(5/25)
TypeError: gcd expected 2 arguments, got 1
>>> math.factorial(5)
120
>>> math.ord(A)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    math.ord(A)
AttributeError: module 'math' has no attribute 'ord'
>>> math.ord('A')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    math.ord('A')
AttributeError: module 'math' has no attribute 'ord'
>>> math.bin(58)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    math.bin(58)
AttributeError: module 'math' has no attribute 'bin'
>>> bin(52)
'0b110100'
>>> hex(52)
'0x34'
>>> oct(58)
'0o72'
>>> dec(0101)
SyntaxError: invalid token
>>> decimal(1010)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    decimal(1010)
NameError: name 'decimal' is not defined
>>> A = 'B'
>>> ord(A)
66
>>> ord(C)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ord(C)
NameError: name 'C' is not defined
>>> ord("C")
67
>>> gcd(5,25)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    gcd(5,25)
NameError: name 'gcd' is not defined
>>> math.gcd(5,15)
5
>>> a=10
>>> b=-12
>>> math.copysign(a,b)
-10.0
>>> a="Nisu"
>>> a[:-1]
'Nis'
>>> a[::-1]
'usiN'
>>> 
