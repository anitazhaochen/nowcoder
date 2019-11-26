#!/usr/bin/python env
# coding:utf8
import random

def insert_sort(nums):
    if (not nums) and (len(nums) < 2):
        return nums
    for i in range(1,len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]


nums = [int(random.random()*100) for i in range(10)]

insert_sort(nums)

print(nums)
