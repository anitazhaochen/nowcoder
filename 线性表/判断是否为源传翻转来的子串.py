#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        if len(s1) != len(s2) or len(s1) == 0:
            return False
        s1 = s1+s1
        flag = False
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                flag = True
                for j in range(len(s2)):
                    if s1[i+j] != s2[j]:
                        flag = False
                        break
                if flag != False:
                    return True
        return False
