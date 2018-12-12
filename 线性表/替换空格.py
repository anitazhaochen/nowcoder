#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s is None or len(s) == 0:
            return s
        count = 0
        for char in s:
            if char == " ":
                count += 1

        res = [0] * (count * 2 + len(s))

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                res[i+count*2] = '0'
                res[i-1+count*2] = '2'
                res[i-2+ count*2] = '%'
                count -= 1
            else:
                res[i+count*2] = s[i]

        return ''.join(res)


print(Solution().replaceSpace('We Are Happy.'))

