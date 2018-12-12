#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):

        if not self.stack1:
            return None
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        res = self.stack1.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res
