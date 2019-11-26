#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  {[(}])

def solution(s):
    if s == None:
        return True
    di = {'(':')', '[':']', '{':'}'}
    stack1 = []
    stack2 = []
    for char in s:
        if char in di.keys():
            stack1.append(char)
        if char in di.values():
            tmp = stack1.pop()
            if di.get(tmp) != char:
                return False

    return True

def solution1(s):
    if s == None:
        return True
    di = {'(':')', '[':']', '{':'}'}
    stack = []
    queue = []
    for char in s:
        if char in di.keys():
            stack.append(char)
        if char in di.values():
            queue.append(char)

    if len(stack) != len(queue):
        return False
    for _ in range(len(stack)):
        left = stack.pop()
        right = queue.pop()
        if di.get(left) != right:
            return False
    return True


def solution2(s):
    if s is None:
        return True
    di = {}
    DI = {'(':')', '[':']', '{':'}'}
    for char in s:
        if char in ['(',')','[',']', '{', '}']:
            if char not in di:
                di[char] = 1
            else:
                di[char] += 1

    for char in DI.keys():
        if di.get(char) != di.get(DI.get(char)):
            return False

    return True




if __name__ == "__main__":
    s = "(({})())"
    # print(solution(s))
    print(solution1(s))
    s = "{[(}])"
    # print(solution(s))
    print(solution1(s))
