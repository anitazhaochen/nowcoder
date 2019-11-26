#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Partition:
    # 这样做无法保证原始顺序
    def partition(self, pHead, x):
        # write code here
        if pHead is None:
            return pHead
        node = pHead
        count = 0
        allcount = 0
        while node:
            if node.val < x:
                count += 1
            allcount += 1
            node = node.next
        if count == 0 or allcount == count:
            return pHead

        node = pHead
        for _ in range(count):
            node = node.next
        midnode = node.next

        node = pHead

        while node and midnode:
            tmp = midnode.val
            while node.val < x and node:
                node = node.next
            while midnode.val >= x and midnode:
                midnode = midnode.next
            if node and midnode:
                node.val, midnode.val = midnode.val, node.val
        return pHead

    def partition1(self, pHead, x):
        if pHead is None:
            return pHead

        node = pHead
        smallhead = ListNode(0)
        bighead = ListNode(0)
        small = smallhead
        big = bighead
        while node:
            if node.val < x:
                small.next = ListNode(node.val)
                small = small.next
            else:
                big.next = ListNode(node.val)
                big = big.next
            node = node.next

        small.next = bighead.next
        return smallhead.next


