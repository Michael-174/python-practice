#__str__
class Student(object):
    def __init__(self, name):
         self.name = name
    def __str__(self):
         return 'Student object (name: %s)' % self.name #这样子print此class时就不会是ID了
    __repr__ = __str__ #用str绑定repr，这样就可以都显示字符串了

# a = Student('Michael')
# print(a) #在控制台中直接敲a还是会给代码，因为直接a调用的时__repr__, 给开发者看的

##################################################################################################

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # # 初始化两个计数器a，b
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
# for x in Fib():
#     print(x)

class countdown(object):
    def __init__(self, count=10):
        self.count = count
    def __iter__(self):
        self.current = self.count
        return self
    def __next__(self):
        if self.current <= 0: raise StopIteration()
        value = self.current
        self.current -= 1
        return value
# for x in countdown():
#     print(x)

class display(object):
    def __init__(self, data = (1,2,3,4,5)):
        self.data = data
    def __iter__(self):
        return iter(self.data)
# x = display()
# x.__iter__()

list = [1,2,3,4,5,6,7]
i = list.__iter__()
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break

###################################################################################################

alist = [1,2,3,4,5]
# print(alist.__getitem__(1))

class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if index >= len(self.data):
            raise IndexError
        return self.data[index]
# for x in MyList([1,2,3]):
#     print(x)

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
# Fib = Fib()
# print(Fib[100])

#####切片#####
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# fib = Fib()
# print(fib[:10])

#######################################################################################
#__setitem__ & __delitem__
num = [1,2,3,4,5]
num.__setitem__(3,3)
# print(num)
num.__delitem__(3)
# print(num)

#######################################################################################
#__getattr__
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return lambda: 100
        raise AttributeError("nigga")
# s = Student()
# print(getattr(s, 'name'))
# # print(s.name)
# print(s.score)
# print(s.score())
# print(s.age)


class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
# print(Chain().apple.nigga.michael)

##############################################################################
#__call__ 把实例当作函数call出来
class Class(object):
    def __init__(self):
        self.name = 'Michael'
    def __call__(self):
        print("hello", self.name)
c = Class()
c()
print(callable(c)) #可以用callable来判断此对象是否是可调用对象




