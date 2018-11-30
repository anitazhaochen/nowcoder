#!/usr/bin/env python
# -*- coding: utf-8 -*-


class queue2stack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def get(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        res = self.q1.pop(0)

        while len(self.q2) > 0:
            self.q1.append(self.q2.pop(0))
        return res

    def put(self, val):
        self.q1.append(val)



if __name__ == "__main__":

    q = queue2stack()


    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q.get())
    q.put(4)
    q.put(6)
    print(q.get())
    q.put(7)
    print(q.get())

