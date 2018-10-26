#!/bin/python env
# coding:utf8



# 依照 Python 官方文档的说法，__new__ 方法主要是当你继承一些不可变的 class 时（比如 int，str，tuple），提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的 metaclass。

# 假如我们需要实现一个永远是正数的整数类型，通过集成 int ，可以这样

class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

i = PositiveInteger(-2)
print i

# 还可以自定义 metaclass 。

# 用 __new__ 来实现单例

class Singleton(object):
    def __new__(cls):
        # 关键在于，每一次实例的时候，我们都只会返回这同一个对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls) # python2.x 写法
            cls.instance = super().__new__(cls) # python3.x 写法
            return cls.instance


