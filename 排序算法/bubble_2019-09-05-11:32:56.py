# coding:utf-8
import random

def is_correct(nums, compare):
    nums.sort()
    for i in range(len(nums)):
        if nums[i]  != compare[i]:
            return False
    return True

def bubble(nums):
    if not (nums and len(nums)>1):
        return nums
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def generate_nums(count=10):
    return [ int(random.random()*100) for i in range(count) ]



nums = generate_nums(10)

result = bubble(nums)
print(result)

