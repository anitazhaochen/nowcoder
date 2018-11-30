#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from myutils import *

@compare
def bubbleSort(arr):
    if arr is None or len(arr) == 0:
        return
    length = len(arr)
    for i in range(0,length):
        for j in range(0,length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = getRandom(-999, 999, 10)
    print(bubbleSort(arr))
