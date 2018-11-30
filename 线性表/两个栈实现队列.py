#!/usr/bin/env python
# -*- coding: utf-8 -*-

class stack2queue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def put(self, val):
        self.s1.append(val)

    def get(self):

        while len(self.s1) > 1:
            tmp = self.s1.pop()
            self.s2.append(tmp)
        res = self.s1.pop()
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res



if __name__ == "__main__":
    qu = stack2queue()
    qu.put(1)
    print(qu.get())
    qu.put(2)
    qu.put(3)
    print(qu.get())
    qu.put(4)
    qu.put(5)
    print(qu.get())
    print(qu.get())
