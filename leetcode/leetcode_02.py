#!/usr/bin/python env
# coding:utf8

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

链接：https://leetcode-cn.com/problems/add-two-numbers
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
#    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#        tmp_l1 = l1
#        tmp_l2 = l2
#        i = 0
#        while tmp_l1.next:
#            i += 1
#            tmp_l1 = tmp_l1.next
#        j = 0
#        while tmp_l2.next:
#            j += 1
#            tmp_l2 = tmp_l2.next
#
#        while tmp_l1.next or tmp_l2.next:
#        if i>j:
#            for _ in range(i-j):
#                tmp_l2.next = ListNode(0)
#                tmp_l2 = tmp_l2.next
#        if j>i:
#            for _ in range(j-i):
#                tmp_l1.next = ListNode(0)
#                tmp_l1 = tmp_l1.next
#
#        head = ListNode(0)
#        node = head
#        value = 0
#        while l1 and l2:
#            print(str(l1.val) + '  '+ str(l2.val) )
#            value = l1.val + l2.val + (0 if value<10 else 1)
#            node.next = ListNode(value%10)
#            node = node.next
#            l1 = l1.next
#            l2 = l2.next
#        if value >= 10:
#            node.next = ListNode(1)
#        # print(result)
#        if head.next:
#            return head.next
#        else:
#            return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_l1 = []
        list_l2 = []
        while l1:
            list_l1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list_l2.append(str(l2.val))
            l2 = l2.next
        list_l1.reverse()
        list_l2.reverse()
        result = list(str(int(''.join(list_l1)) +
                     int(''.join(list_l2))))
        result.reverse()
        head = ListNode(0)
        node = head
        for i in result:
            node.next = ListNode(int(i))
            node = node.next

        return head.next



l1 = ListNode(9)
l1.next = ListNode(9)
#l1.next.next = ListNode(3)

l2 = ListNode(1)
#l2.next = ListNode(9)
#l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1, l2))

