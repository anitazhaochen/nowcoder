#!/usr/bin/env python
# -*- coding: utf-8 -*-

from myutils import *


@compare
def selectSort(arr):
    if arr is None or len(arr) == 0:
        return

    length = len(arr)
    for i in range(0, length-1):
        min = i
        for j in range(i+1, length):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


if __name__ == "__main__":
    arr = getRandom()
    print(selectSort(arr))

