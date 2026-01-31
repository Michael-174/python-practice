def calc_sum(*nigga): # *把输入的参数封装成一个tuple
    ax = 0
    for n in nigga:
        ax = ax + n
    return ax #普通函数
print(calc_sum(1,2,3,4,5,6,7,8,9,10))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax #返回的函数内部用返回
    return sum #用函数返回
result = lazy_sum(1,2,3,4,5,6,7,8,9,10)
print(result) #不会打印结果而是函数
print(result()) #调用函数result时才是结果
print(lazy_sum(1,2,3,4,5,6,7,8,9,10)()) # 等价于调用result
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f1 = lazy_sum(1,2,3,4,5,6,7,8,9,10)
f2 = lazy_sum(1,2,3,4,5,6,7,8,9,10)
print(f1 == f2) #即使参数一样每一次的函数都是不一样的，因为函数每次创建都是一个新的ID
print(f1() == f2()) #调用函数输出的值自然是一样的

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
a,b,c = count()
print(a(), b(), c()) #会输出三个九是因为闭包会延时绑定，引用的参数时函数外的循环，当循环结束时i = 3，所以全都会引用3

def count():
    def f(j):
        def g():
            return j*j
        return g    #因此，可以再创建一个函数来绑定循环变量
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
a,b,c = count()
print(a(), b(), c())

def count():
    return [ (lambda j=i: j*j) for i in range(1, 4) ] #可以用lambda超级简化
