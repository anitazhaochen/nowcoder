    #!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def solution(arr):
    length = len(arr)
    has_num = [0 for _ in range(length+1)]

    arr_max_and_min = [{'amax':0,'amin':0} for _ in range(length+1)]

    arr_min = min(arr)
    arr_max = max(arr)
    arr_max_and_min[0]['amin'] = arr_min
    arr_max_and_min[0]['amax'] = arr_min
    arr_max_and_min[-1]['amax'] = arr_max
    arr_max_and_min[-1]['amin'] = arr_max
    has_num[0] = 1
    has_num[-1] = 1
    for num in arr:
        res = to(arr_min, arr_max, length, num)
        print(num)
        print(res)
        if has_num[res] == 0:
            arr_max_and_min[res]['amax'] = num
            arr_max_and_min[res]['amin'] = num
            has_num[res] = 1
        else:
            arr_max_and_min[res]['amax'] = num if num > arr_max_and_min[res]['amax'] else arr_max_and_min[res]['amax']
            arr_max_and_min[res]['amin'] = num if num < arr_max_and_min[res]['amin'] else arr_max_and_min[res]['amin']

    i = 0
    res = []
    res_min = arr_max_and_min[0]['amax']
    while i < length+1:
        while i < length+1 and has_num[i] == 0:
            i += 1
        if i < length+1:
            res_max = arr_max_and_min[i]['amin']
            res.append(res_max- res_min)
            res_min = arr_max_and_min[i]['amax']
            i += 1

    print(res)
    print(arr_max_and_min)
    return max(res)



def to(arr_min, arr_max, length, num):
    tmp = int((arr_max - arr_min)/(length+1))+1
    print("TMP")
    print(arr_min)
    print(arr_max)
    print(tmp)
    result = (num-arr_min) // tmp
    return result



if __name__ == "__main__":
    arr = [random.randint(0,999) for _ in range(10) ]
    result = solution(arr)
    arr = sorted(arr)
    max = arr[0] - arr[1]
    for i in range(len(arr)-1):
        if max < arr[i+1] - arr[i]:
            max = arr[i+1] - arr[i]

    print(arr)
    if result == max:
        print("sucess")
    else:
        print("正确答案")
        print(result)
        print(max)
        print("failed")








