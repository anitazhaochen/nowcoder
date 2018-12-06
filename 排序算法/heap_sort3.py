#!/usr/bin/env python
# -*- coding: utf-8 -*-

import myutils


def build_heap(arr):
    heapsize = len(arr)
    for i in range((heapsize-2)//2, -1, -1):
        heapify(arr, i, heapsize)

def heapify(arr, root, heapsize):
    left = root * 2 + 1
    right = left + 1
    large = root
    if left < heapsize and arr[large] < arr[left]:
        large = left
    if right < heapsize and arr[large] < arr[right]:
        large = right

    if large != root:
        arr[large], arr[root] = arr[root], arr[large]
        heapify(arr, large, heapsize)


@myutils.compare
def heapSort(arr):
    heapsize = len(arr)
    build_heap(arr)
    for i in range(heapsize-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

if __name__ == "__main__":

    arr = myutils.getRandom()
    print(heapSort(arr))
