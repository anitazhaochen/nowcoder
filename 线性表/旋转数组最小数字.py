#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def minNumberInRotateArray(self, rotateArray):

        if rotateArray is None or len(rotateArray) == 0:
            return 0

        left = 0
        right = len(rotateArray) - 1
        while left < right-1:
            # mid = (left+right) // 2
            mid = left + (right-left) // 2 # 防止溢出
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            if rotateArray[mid] <= rotateArray[right]:
                right = mid

        return rotateArray[right]




print(Solution().minNumberInRotateArray([6,1,2,3,4,5]))

