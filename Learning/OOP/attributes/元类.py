#type()
x = 10
# print(type(x)) #type最常见的用法是判定其类型

#type还可以动态创建类
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))