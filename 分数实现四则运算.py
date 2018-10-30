#!/bin/python env
# coding:utf8

from fractions import Fraction


a = raw_input()
if ' ' in a:
    a = a.split(' ')
    x,y = a[1].split('/')
    c = int(y)*int(a[0]) + (int(x) if int(a[0]) > 0 else -(int(x)))
    a1 = Fraction(c,int(y))
elif "/" in a:
    x,y = a.split('/')
    a1 = Fraction(int(x),int(y))
else:
    a1 = Fraction(int(a),1)


b = raw_input()

a = raw_input()
if ' ' in a:
    a = a.split(' ')
    x,y = a[1].split('/')
    c = int(y)*int(a[0]) + (int(x) if int(a[0]) > 0 else -(int(x)))
    a2 = Fraction(c,int(y))
elif "/" in a:
    x,y = a.split('/')
    a2 = Fraction(int(x),int(y))
else:
    a2 = Fraction(int(a),1)


if b == '+':
    res = a1+a2
if b == '-':
    res = a1-a2
if b == '*':
    res = a1*a2
if b == '/':
    res = a1/a2

x = res.numerator
y = res.denominator
if x == 0:
    print str(0)
elif abs(x) >= y :
    tmp = abs(x) % y
    if tmp == 0:
        print str(x/y)
    else:
        tmp2 = abs(x) / y
        print "-"+str(tmp2)+" "+str(tmp)+"/"+str(y) if x < 0 else str(tmp2)+" "+str(tmp)+"/"+str(y)
else:
    print str(x)+"/"+str(y)

# 小马智行    100% AC


