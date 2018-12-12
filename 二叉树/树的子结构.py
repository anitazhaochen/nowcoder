#!/usr/bin/env python
# -*- coding: utf-8 -*-


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#class Solution:
#    def HasSubtree(self, pRoot1, pRoot2):
#        root1 = pRoot1
#        root2 = pRoot2
#        queue = [root1]
#        while queue:
#            node = queue.pop(0)
#            if node.val == pRoot2.val:
#                return self.compare(root1, root2)
#            if node.left:
#                queue.append(node.left)
#            if node.right:
#                queue.append(node.right)
#        return False
#
#
#    def compare(self,root1, root2):

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.is_subtree(pRoot1.left, pRoot2) or self.is_subtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self.is_subtree(pRoot1.left, pRoot2.left) and self.is_subtree(pRoot1.right, pRoot2.right)


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
root1.left.left.left = TreeNode(8)
root1.left.left.right = TreeNode(9)


root2 = TreeNode(4)
root2.left = TreeNode(8)
root2.right = TreeNode(9)

res = Solution().HasSubtree(root1, root2)
print(res)
