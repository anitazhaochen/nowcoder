#!/bin/python env
# coding:utf8

def heapSort(arr):
    if arr == None or len(arr) < 2:
        return 
    for i in range(len(arr)):
        heapInsert(arr, i)

    size = len(arr)
    size -= 1
    swap(arr, 0, size)

    while size > 0:
        heapify(arr, 0, size)
        index = (index - 1) / 2


def heapify(arr, index, size):
    left = index * 2 + 1
    while left<size:
        largest = left + 1 if left + 1 < size and arr[left+1] > arr[left] else left
        if largest == index:
            break

        swap(arr,largest, index)
        index = largest
        left = index * 2 + 1

def swap(arr, i , j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def heapInsert(arr, index):
    while arr[index] > arr[(index-1)/2]:
        swap(arr, index, (index-1)/2)
        index = (index-1)/2



def solution(arr):
    arr = map(int, raw_input().split(' '))
    arr,k = sorted(arr[:-1]),arr[-1]
    print " ".join(map(str,arr[:k]))
    
