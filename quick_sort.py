#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myutils import *

def quickSort(arr, start, end):
    if start >= end:
        return
    left = start
    right = end
    mid = arr[left]
    while left < right:
        while arr[right] >= mid and right > left:
            right -= 1
        arr[left] = arr[right]
        while arr[left] <= mid and left < right:
            left += 1
        arr[right] = arr[left]

    arr[left] = mid
    quickSort(arr,start,left-1)
    quickSort(arr, left+1,end)


if __name__ == "__main__":
    for _ in range(100):
        arr = [random.randint(-999,999) for _ in range(10) ]
        arr1 = copy.deepcopy(arr)
        arr1 = sorted(arr1)
        quickSort(arr,0,len(arr)-1)
        if arr1 != arr:
            print(arr1)
            print(arr)
            print("failed")
            exit()
    print("success")


