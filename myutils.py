#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import copy

def getRandom(start=-999, end=999, count=10):
    return [random.randint(start,end) for _ in range(count)]


def compare(func):
    def wrap(arr):
        arr2 = copy.deepcopy(arr)
        arr2 = sorted(arr2)
        print(arr2)
        func(arr)
        print(arr)
        return "sucess" if arr == arr2 else "failed"
    return wrap
