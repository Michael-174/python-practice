#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""此module的用途是用来测试module的调用，内涵可以根据cmd参数打印greeting的test()函数，Michael人生中第一个module"""
__author__ = 'Michael Ju'
__name__ = "nigga"
import sys
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()

#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名

