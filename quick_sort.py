#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myutils import *

def quickSort(arr, start, end):
    if end - start <= 1:
        return
    left = start
    right = end
    mid = arr[left]
    while left < right:
        while arr[left] < mid and left < end:
            left += 1
        while arr[right] > mid and right > start:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]

    mid, arr[left] = arr[left], mid
    quickSort(arr,start,left)
    quickSort(arr, left+1,end)


if __name__ == "__main__":
    arr = getRandom()
    quickSort(arr,0,9)
    print(arr)


