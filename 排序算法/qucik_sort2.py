#!/usr/bin/env python
# -*- coding: utf-8 -*-
import myutils

def quickSort(arr, start, end):
    if start >= end:
        return

    left = start
    right = end
    select = arr[start]

    while left < right:
        while arr[right] >= select and right > left:
            right -= 1
        arr[left] = arr[right]

        while arr[left] <= select and left < right:
            left += 1
        arr[right] = arr[left]

    arr[left] = select

    quickSort(arr, start, left-1)
    quickSort(arr, left+1, end)


if __name__ == "__main__":
    arr = myutils.getRandom()
    quickSort(arr, 0, 9)
    print(arr)
