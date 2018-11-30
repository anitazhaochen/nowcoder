#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myutils import *

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid =  len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(arr1,arr2):
    left = 0
    right = 0
    arr = []
    while left < len(arr1) and right < len(arr2):
        if arr1[left] <= arr2[right]:
            arr.append(arr1[left])
            left += 1
        else:
            arr.append(arr2[right])
            right += 1
    #while left < len(arr1):
    #    arr.append(arr1[left])
    #    left += 1
    #while right < len(arr2):
    #    arr.append(arr2[right])
    #    right += 1
    arr += arr1[left:]
    arr += arr2[right:]
    print(arr)
    return arr


if __name__ == "__main__":
    arr = getRandom(1,100,3)
    print(arr)
    print(mergeSort(arr))
