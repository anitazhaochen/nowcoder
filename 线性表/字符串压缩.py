#!/usr/bin/env python
# -*- coding: utf-8 -*-


# -*- coding:utf-8 -*-
class Zipper:
    def zipString(self, iniString):
        # write code here
        s = ''
        curr = iniString[0]
        count = 0
        for char in iniString:
            if char == curr:
                count += 1
            else:
                s += curr + '' + str(count)
                curr = char
                count = 1
        s += curr+''+str(count)
        if len(s) >= len(iniString):
            return iniString
        else:
            return s


s = Zipper().zipString('abc')
print(s)
