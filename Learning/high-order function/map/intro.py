a = abs
print(a) #可以把一个函数赋值给另一个
print(a(10))
#函数名同时也是变量

def add(x, y, f):
    return f(x) + f(y)  #一个函数接收另一个函数作为参数
print(add(-100, 100, abs))

