    #!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
import random
import copy

def quickSort(arr,start, end):
    if end <= start :
        return

    select = arr[start]
    left = start
    right = end
    while left < right:
        while arr[right] >= select and right > left:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= select:
            left += 1
        arr[right] = arr[left]

    arr[left] = select
    quickSort(arr, start, left-1)
    quickSort(arr, left+1, end)


def getMiddle(arr):
    def findmiddle(arr, start, end):
        if end <= start:
            return
        select = arr[start]

        left = start
        right = end

        while left < right:
            while arr[right] >= select and right > left:
                right -= 1
            arr[left] = arr[right]
            while arr[left] <= select and left < right:
                left -= 1
            arr[right] = arr[left]
        arr[left] = select
        return left

    result = findmiddle(arr,0, len(arr)-1)
    size = len(arr)
    middle = size // 2

    while result != middle:

        if result < middle:
            result = findmiddle(arr,result+1, len(arr)-1)
        if result > middle:
            result = findmiddle(arr, 0, result-1)

    if size % 2 == 0:
        return (arr[middle]+arr[middle-1])/2
    else:
        return arr[middle]

# 建堆实现
def getmiddle1(arr):
    heap1 = []
    heap2 = []
    size = len(arr) // 2
    heapq.heapify(heap1, arr[:size])
    heapq.heapify(heap2, arr[size:])
    if len(arr) % 2 == 0:
        result = (heapq.heappop(heap1) + heapq.heappop(heap2)) / 2
    else:
        result = heapq.heappop(heap2)

    return result


if __name__ == "__main__":
    for _ in range(100):
        arr = [random.randint(-999,999) for _ in range(10) ]
        arr1 = copy.deepcopy(arr)
        arr1 = sorted(arr1)
        quickSort(arr,0,len(arr)-1)
        if arr1 != arr:
            print(arr1)
            print(arr)
            print("failed")
            exit()
    print("success")

    arr = [1,2,3,4,5,6]
    res = getMiddle(arr)
    print(res)

    print(getmiddle1(arr))

