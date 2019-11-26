#!/usr/bin/python env
# coding:utf8
import random

'''
1.
随机选取一个值，然后跟中间的交换，然后将大于这个数的放一边，小于这个数的放一边
'''


def quick_sort(nums,start,end):
    if start >= end:
        return

    left = start
    right = end
    mid_num = nums[start]
    while end > start:
        # 注意需要加 =  ，因为如果相等不进行 减一的话， 有可能 另一边也是相等，
        # 也不 减一，最后就 end > start 永远成立
        while nums[end] >= mid_num and end > start:
            end -= 1
        nums[start] = nums[end]
        while nums[start] <= mid_num and end > start:
            start += 1
        nums[end] = nums[start]
    nums[start] = mid_num

    quick_sort(nums, left, start-1)
    quick_sort(nums, start+1, right)



nums = [ int(random.random()*100) for i in range(10)]

quick_sort(nums, 0, len(nums)-1)
print(nums)
