#!/usr/bin/env python
# -*- coding: utf-8 -*-


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        p1 = pHead
        p2 = pHead.next
        pHead.next = None
        while p2:
            pre = p1
            p1 = p2
            p2 = p2.next
            p1.next = pre

        return p1


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

node1 = Solution().ReverseList(node)
while node1:
    print(node1.val)
    node1 = node1.next




