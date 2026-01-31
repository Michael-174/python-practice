# def nigga():
#     print("nigga")
# a = nigga
# print(a.__name__) #__name__属性可以拿到函数刚开始创建时的名字
#现在，假设我们要增强nigga()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改nigga()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):  #**收集所有关键词参数并组装成一个dict， *则是所有的位置参数， 其本质时涵盖所有参数
        print('call %s():' % func.__name__)
        return func(*args, **kw) #wrapper把输入的函数wrap起来，再加上装饰品
    return wrapper
@log #装饰器用@调用
def nigga():
    print("nigga")
nigga()

def log(text): #有参数的decorator需要三层嵌套，比较复杂
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log("nigga")
def nigga():
    print("nigga")
nigga()
print(nigga.__name__) #名字是wrapper因为decorator中返回时wrapper，可以用functools中的.wrap()解决

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
# pass
# 又支持：
# @log('execute')
# def f():
# pass
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call")
        func(*args, **kw)
        print("end call")
        return None
    return wrapper


def log(text = "begin call"): #此代码可以实现传参或空参
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f"{str(text)} {func.__name__}:")
            func(*args, **kw)
        return wrapper
    return decorator

def log(text = None):
    if not callable(text):
        text = "begin call"
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(f"{text} {func.__name__}:")
                return func(*args, **kw)
            return wrapper
        return decorator
@log
def nigga():
    print("nigga")
nigga()


