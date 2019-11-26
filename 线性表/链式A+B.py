#!/usr/bin/env python
# -*- coding: utf-8 -*-



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Plus:
    def plusAB(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        head = ListNode(0)
        c = head
        jinwei = 0
        while a or b or jinwei != 0:
            if a is None and b is None:
                tmp = 0 + 0 + jinwei
            elif b is None:
                tmp = a.val + 0 + jinwei
            elif a is None:
                tmp = 0 + b.val + jinwei
            else:
                tmp = a.val + b.val + jinwei

            if tmp >= 10:
                c.next = ListNode(tmp%10)
                jinwei = 1
                c = c.next
            else:
                c.next = ListNode(tmp)
                jinwei = 0
                c = c.next
            if a:
                a = a.next
            if b:
                b = b.next

        return head.next

a = ListNode(1)
a.next = ListNode(1)
#a.next.next = ListNode(3)

b = ListNode(1)
b.next = ListNode(2)

c = Plus().plusAB(a,b)
while c:
    print(c.val)
    c = c.next





