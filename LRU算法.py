#!/bin/python env
# coding:utf8

from collections import OrderedDict

class LRUCache(OrderedDict):
    ''' 不能存储可变类型对象，不能并发访问 set() '''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = -1
        return value

    def set(self, key, value):
        if self.cache.has_key(key):
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last = False)
                self.cache[key] = value
            else:
                self.cache[key] = value

if __name__ == "__main__":
    c = LRUCache(5)
    for i in range(5,10):
        c.set(i, 10*i)
    print c.cache, c.cache.keys()
    c.get(5)
    c.get(7)
    print c.cache, c.cache.keys()

    c.set(10,100)
    print c.cache, c.cache.keys()

    c.set(9,99)
    print c.cache, c.cache.keys()




# 利用 list 和 dict 实现，dict 是无序的，用列表维护顺序。
class LRUCache1(object):
    '''不能存储可变类型对象，不能并发访问 set()'''

    def __init__(self, capacity):
        self.l = []
        self.d = {}
        self.capacity = capacity

    def get(self, key):
        if self.d.has_key(key):
            value = self.d[key]
            self.l.remove(key)
            self.l.insert(0,key)
        else:
            value = -1
        return value

    def set(self, key, value):
        if self.d.has_key(key):
            self.l.remove(key)
        elif len(self.d) == self.capacity:
            oldest_key = self.l.pop()
            self.d.pop(oldest_key)
        self.d[key] = value
        self.l.insert(0, key)
