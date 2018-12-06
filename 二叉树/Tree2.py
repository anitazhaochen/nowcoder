#!/usr/bin/env python
# -*- coding: utf-8 -*-

class tree(object):
    left = None
    right = None
    val = None
    def __init__(self,val):
        self.val = val

    def preOrder(self, root):

        stack = [root]

        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inOrder(self, root):
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            if stack:
                node = stack.pop()
                if node:
                    print(node.val, end=" ")
                    node = node.right


    def postOrder(self, root):
        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            print(stack2.pop().val, end=" ")


    def Serialization(self, root):
        if root is None:
            return "#!"
        res = str(root.val)+"!"
        res += self.Serialization(root.left)
        res += self.Serialization(root.right)
        return res

    def deSerialization(self, s):
        queue = s.strip().split('!')
        # a = "1!2!"  a.split('!') [1,2,''], 所有要放弃最后一个
        return self.a(queue[:-1])

    def a(self, queue):
        print(queue)
        value = queue.pop(0)
        if value == "#":
            return None
        print(value)
        root = tree(value)
        root.left = self.a(queue)
        root.right = self.a(queue)
        return root





if __name__ == "__main__":
    root = tree(1)
    root.left = tree(2)
    root.right = tree(3)
    root.left.left = tree(4)
    root.left.right = tree(5)
    root.right.left = tree(6)
    root.right.right = tree(7)


    root.preOrder(root)
    print()
    root.inOrder(root)
    print()
    root.postOrder(root)

    s = root.Serialization(root)
    s = root.deSerialization(s)
    if s == root:
        print("success")
