#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myutils import getRandom
from myutils import compare

@compare
def insertSort(arr):
    if arr is None or len(arr) == 0:
        return
    length = len(arr)
    for i in range(1, length):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


if __name__ == "__main__":
    arr = getRandom(-999,999, 10)
    print(insertSort(arr))


