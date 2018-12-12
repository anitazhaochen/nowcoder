# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        n = exponent
        if n < 0:
            exponent = -n
        if base == 0:
            return
        if exponent == 0:
            return 1

        curr = base
        res = 1

        while exponent != 0:
            if (exponent&1)==1:
                res *= curr
                print("res:" + str(res))
            curr *= curr
            print("curr"+str(curr))
            exponent >>= 1
        return res if exponent>0 else 1.0/res


Solution().Power(10,13)
