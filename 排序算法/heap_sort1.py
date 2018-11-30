#!/usr/bin/env python
# -*- coding: utf-8 -*-
import myutils


def build_heap(arr):
    heapsize = len(arr)
    for i in range((heapsize-2)//2,-1,-1):
        heapify(arr, heapsize, i)

def heapify(arr, heapsize,root):
    left = root * 2 + 1
    right = left + 1
    larger = root
    if left < heapsize and arr[left] > arr[larger]:
        larger = left
    if right < heapsize and arr[right] > arr[larger]:
        larger = right
    if arr[larger] != arr[root]:
        arr[root], arr[larger] = arr[larger], arr[root]
        heapify(arr, heapsize, larger)

@myutils.compare
def heap_sort(arr):
    heapsize = len(arr)
    build_heap(arr)
    for i in range(heapsize-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


if __name__ == "__main__":

    arr = myutils.getRandom()
    print(heap_sort(arr))

