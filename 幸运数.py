#!/usr/bin/python env
# coidng:utf8


n = input()
count = 0
for i in range(1,n+1):
    if sum(map(int,list(str(bin(i)))[2:])) == sum(map(int,list(str(i)))):
        count += 1
print count

