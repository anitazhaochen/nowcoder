#!/usr/bin/env python
# -*- coding: utf-8 -*-
import myutils


def build_heap(arr):
    heapsize = len(arr)
    for i in range((heapsize-2)//2, -1, -1):
        heapify(arr, heapsize, i)



def heapify(arr, heapsize, root):
    left = root * 2 + 1
    right = left + 1
    large = root
    if left < heapsize and arr[left] > arr[large]:
        large = left
    if right < heapsize and arr[right] > arr[large]:
        large = right

    if arr[large] != arr[root]:
        arr[root],arr[large] = arr[large], arr[root]
        heapify(arr, heapsize, large)


@myutils.compare
def heapSort(arr):
    heapsize = len(arr)
    build_heap(arr)
    for i in range(heapsize-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)



if __name__ == "__main__":

    arr = myutils.getRandom()
    print(heapSort(arr))

