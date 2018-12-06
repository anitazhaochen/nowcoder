#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Hanoi:
    def chkStep(self, arr, n):
        # write code here
        self.cur_status = [1] * n  # 初始状态，所有的圆盘都在左柱上
        self.moves = []  # 记录所有的cur_status
        self.moves.append(self.cur_status[:])
        self.solve(n, 1, 2, 3)

        i = 0
        #print(self.moves)
        for status in self.moves:
            if arr == status:
                return i
            i += 1
        return -1

    def move(self, n, s2):
        self.cur_status[n - 1] = s2
        print(self.cur_status)
        self.moves.append(self.cur_status[:])

    def solve(self, n, s1, s2, s3):
        if n == 1:
            self.move(n, s3)
        else:
            self.solve(n - 1, s1, s3, s2)  # 移动上面n-1个到中柱（左柱到中柱）
            self.move(n,s2)  #
            self.solve(n - 1, s2, s1, s3)  # 中柱到右柱

Hanoi().chkStep([3,3,3,3,3],5)
