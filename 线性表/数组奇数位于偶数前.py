# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if array is None or len(array) == 0:
            return []

        for i in range(len(array)):
            for j in range(0,len(array)-i-1):
                if array[j]%2 == 0 and array[j+1]%2!=0:
                    array[j],array[j+1] = array[j+1], array[j]
        return array



print(Solution().reOrderArray([1,2,3,4,5,6]))