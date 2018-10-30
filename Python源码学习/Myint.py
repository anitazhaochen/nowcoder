#!/bin/python env
# coding:utf8


'''
凡是在类中定义了　__getitem__　方法，那么它的实例对象(假定为Ｐ)，就可以像　P[key]　取值，当实例对象做 P[key] 运算时，会调用类中的方法　__getitem__ 。
'''

class MyInt(int):
    def __getitem__(self, key):
        return key + str(self)


a = MyInt(1)
b = MyInt(2)
print a+b
print a['key']


''' 
这样的操作是一个类似于　dict　的对象才会支持的操作。可以通过重写 __getitem__　这个 Python 中的　special method，可以视为指定了　Ｍyint 在　Python 内部对应的　PyTypeObject 对象的 tp_as_mapping.mp_subscript 操作。最终的结果是　Myint 的实例对象可以“表现”得像一个关联对象一样，归根结底就在于　PyTypeObject 中允许一种类型同时指定三种不同对象的行为特性。

'''
