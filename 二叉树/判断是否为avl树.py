#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Balance:
    def isBalance(self, root):
        return self.get_deep(root) != -1

    def get_deep(self,root):
        if root is None:
            return 0
        left = self.get_deep(root.left)
        if left == -1:
            return -1
        right = self.get_deep(root.right)
        if right == -1:
            return -1
        if abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1