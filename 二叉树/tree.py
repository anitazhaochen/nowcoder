#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tree(object):
    left = None
    right = None
    val = None
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.val, end=" ")
        self.inOrder(root.right)

    def preOrder(self, root):
        if root is None:
            return
        print(root.val,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def posOrder(self, root):
        if root is None:
            return
        self.posOrder(root.left)
        self.posOrder(root.right)
        print(root.val,end=" ")

    def rebuild_tree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return Tree(preorder[0])
        else:
            root = Tree(preorder[0])
            index = inorder.index(preorder[0])
            root.left = self.rebuild_tree(preorder[1: inorder.index(preorder[0])+1],inorder[:inorder.index(preorder[0])])
            root.right = self.rebuild_tree(preorder[inorder.index(preorder[0])+1:],inorder[inorder.index(preorder[0])+1:])
        return root

    # 按行打印二叉树
    def printTree(self, root):
        queue = [root]
        last = root
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
                nlast = node.left
            if node.right:
                queue.append(node.right)
                nlast = node.right

            if node == last:
                print()
                last = nlast

    # 二叉树前序遍历非递归
    def norecpre(self, root):
        stack = [root]
        res = ""
        while len(stack):
            node = stack.pop()
            print(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

    def noreinorder(self, root):
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

    def noreposorder(self, root):
        stack1 = [root]
        preNode = None
        stack2 = []
        while stack1:
            node = stack1[-1]
            if ((node.left is None) and  (node.right is None)) or \
                ((preNode) and (preNode == node.right or preNode == node.left)):
                print(node.val, end=" ")
                stack1.pop()
                preNode = node
            else:
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)

    def noreposorder2(self, root):
        stack1 = [root]
        node = root
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            print(stack2.pop().val)




if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.left = Tree(6)
    root.right.right = Tree(7)

    root.preOrder(root)
    print()
    root.inOrder(root)
    print()
    root.posOrder(root)
    print()
    abc = root.rebuild_tree([1 ,2 ,4 ,5 ,3 ,6 ,7],[4 ,2 ,5 ,1 ,6 ,3 ,7])
    root.preOrder(abc)
    print("111")
    root.printTree(root)
    print("AAAAAAAA")
    #root.serialization(root)
    root.noreinorder(root)
    print("BBBB")
    root.noreposorder(root)
    print("CCCCCC")
    root.noreposorder(root)
