#__str__
class Student(object):
    def __init__(self, name):
         self.name = name
    def __str__(self):
         return 'Student object (name: %s)' % self.name #这样子print此class时就不会是ID了
    __repr__ = __str__ #用str绑定repr，这样就可以都显示字符串了

a = Student('Michael')
print(a) #在控制台中直接敲a还是会给代码，因为直接a调用的时__repr__, 给开发者看的

##################################################################################################

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # # 初始化两个计数器a，b
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值

