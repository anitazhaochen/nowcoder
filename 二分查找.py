#!/usr/bin/python env
# coding:utf8

def solution(arr, num):
    low = 0
    height = len(arr) - 1
    while low <= height:
        mid = (low+height) / 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            height = mid - 1
        else:
            return mid
    return -1

print solution([1,2,3,4,5,6,7], 10)
