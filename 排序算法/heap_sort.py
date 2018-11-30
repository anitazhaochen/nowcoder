#!/usr/bin/env python
# -*- coding: utf-8 -*-
import myutils


def Build_MAX_Heap(heap):
    HeapSize = len(heap)
    for i in range((HeapSize-2)//2,-1,-1):
        MAX_Heapify(heap, HeapSize, i)


def MAX_Heapify(heap, HeapSize, root):
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        MAX_Heapify(heap, HeapSize, larger)


@myutils.compare
def HeapSort(heap):
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

if __name__ == "__main__":
    arr = myutils.getRandom()
    print(HeapSort(arr))

