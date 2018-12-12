#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return root

        queue = [root]
        li = []
        while queue:
            node = queue.pop(0)
            li.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        while li:
            node = li.pop(0)
            node.left, node.right = node.right, node.left

        return root

    def Mirror1(self,root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror1(root.left)
        if root.right:
            self.Mirror1(root.right)
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

Solution().Mirror1(root)

print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)
print(root.right.right.val)




