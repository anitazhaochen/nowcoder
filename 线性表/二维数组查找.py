#!/usr/bin/env python
# -*- coding: utf-8 -*-


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array is None or target is None or len(array) <= 0:
            return False
        size = len(array)
        right = 0
        left = size - 1
        while right < size and left > -1:
            if target > array[right][left]:
                right += 1
            elif target < array[right][left]:
                left -= 1
            else:
                return True
        return False



print(Solution().Find(5,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))

