#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_heap(arr):
    heapsize = len(arr)
    for i in range((heapsize-2)//2,-1,-1):
