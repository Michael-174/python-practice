#try可以尝试执行某段代码，然后如果出错就会停止并执行except的代码，最后执行finally的代码
try:
    print("try...")
    r = 10/2 #10/2 如果执行没问题except就不会执行
    print("10/0 = ",r)
except ZeroDivisionError as e:
    print('except:', e)
else: #如果没有错就会执行else的代码
    print('noo error')
finally: #无论如何都会执行
    print("finally...")
print('end')

#############################################################################

# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
# main() #其错误会从下到上持续报错直至找到此源头，这是一个堆栈

import logging #logging可以错误堆栈打印出来，同时让程序继续执行
#logging还可以把错误记录下来
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s) * 2

def main():
    try:
        bar("0")
    except Exception as e:
        logging.exception(e)
# main()
# print("end")

#######################################################################################

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
# foo('0')

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()





