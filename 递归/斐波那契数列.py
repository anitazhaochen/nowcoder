#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci1(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1

        for i in range(n):
            a, b = b, a+b
        return a

    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1

        return 2 * self.jumpFloorII(number-1)


    def jump(self ,number):
        i = 1
        return i << (number - 1)

    def rectCover(self, number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.rectCover(number - 1) + self.rectCover(number - 2)

    def rectCover1(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        p = 1
        q = 2
        for i in range(2, number):
            q, p = p + q, q
        return q


print(Solution().Fibonacci(10))
print(Solution().Fibonacci1(10))
print(Solution().jumpFloorII(4))
for i in range(20):
    if Solution().rectCover(i) != Solution().rectCover1(i):
        print('failed')
        break

