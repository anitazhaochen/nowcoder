#!/usr/bin/python env
# coding:utf8

def solution(arr):
    if arr is None or len(arr) == 0:
        return arr
    zeroCount = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroCount += 1
        elif zeroCount!=0:
            arr[i-zeroCount] = arr[i]
            arr[i] = 0
        else:
            pass
    return arr


print solution([0,1,0,3,12])
