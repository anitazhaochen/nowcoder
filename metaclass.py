#coding:utf8

class C(type):
    def __new__(cls, name, bases, attrs):
        for key in attrs.keys():
            attrs.pop(key)
        #print attrs
        #print str(bases)+"new 执行完毕"
        return type.__new__(cls, name, bases, attrs)
    def __init__(cls, name, bases, attrs):
        print "i am metaclass init"
        #print 'and'+ str(kwargs)
        super(C,cls).__init__(name, bases, attrs)

    #def __call__(cls, *args, **kwargs):
    #    print "I am call"
    #    print kwargs

class E(object):
    def __init__(self,*args, **kwargs):
        print "EEEEEEEEEEEEEEEEEEE"

    def __call__(cls, *args, **kwargs):
        print "E call"
        print kwargs



class A(E):
    __metaclass__ = C
    a = 1
    def __init__(self, **args):
        #super(A, self,).__init__()
        print "AAAAAAAAAAAAA"
        #print "开始执行 A的 init"
        #print args
        #super(A, self).__init__(**kw)

    def __call__(cls, *args, **kwargs):
        print "A  call"
        print kwargs




class B(A):
    name = 1

    def __init__(self,*args,**kwargs):
        print "BBBBB"


#class D(B):
#    pass

b = B(name='111')
#b =  B.__new__()
#print id(B.__new__)
#print id(A.__new__)
#print C.__init__ is B.__init__


'''
metaclass 在 django 的 orm 中用的比较多。
他的调用顺序是，在创建类的时候就加载，即使不 创建任何对象。
创建对象的时候，会去调用  metaclass 中的 __call__ 方法，如果次方法不存在，则调用 指向 metaclass 类 自己的 父类的 __init__ 方法。

详情：  https://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/
'''
