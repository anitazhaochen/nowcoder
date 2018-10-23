#!/usr/bin/python env
# coidng:utf8


n = input()
count = 0
for i in range(1,n+1):
    n1 = map(int,list(str(bin(i)))[2:])
    n1 = sum(n1)
    n2 = map(int,list(str(i)))
    n2 = sum(n2)
    if n1 == n2:
        count += 1

print count

