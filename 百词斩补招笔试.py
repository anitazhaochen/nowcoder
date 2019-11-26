#!/usr/bin/env python
# -*- coding: utf-8 -*-



# 因为 Python 和 c 语言的 字符串类型不同，所以，我用 Python 模拟 char[] 类型进行实现

def solution(s):
    if len(s) == 0:
        return None
    s = list(s)
    current = s[0]
    count = 0
    result = ""
    for char in s:
        if current == char:
            count += 1
        else:
            if count == 1:
                result += current
            else:
                result += current + str(count)
            current = char
            count = 1
    if count == 1:
        result += current
    else:
        result += current+ str(count)
    return result

if __name__ == "__main__":
    s = raw_input()
    print solution(s)