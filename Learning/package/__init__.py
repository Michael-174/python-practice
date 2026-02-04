"""此package的用途是用来学习结构和调用，内涵可以module1，可以根据cmd参数打印greeting的test()函数。Michael人生中第一个package"""
__author__ = 'Michael J'

print("package imported!")
#此__init__文件在每次创建包时都会创建，其目的时初始化包，每次包被调用，__init__里的内容会先被调用
#调用包的时候，可以直接调用此文件中的内容，比如package.hello()

def hello(x):
    print(f"hello {x}")

#此文件同时可以控制控制“从包导入什么”，从而减去from xxx.xxx.xxx.package import xxx 的麻烦
#同时也可以控制用户，让用户看到该看的

from .module1 import test #import package后无需再import module1 就可以使用test（），注意module1前面要加. 表示相对导入，否则会报错
#.表示当前包，..表示父包，...以此类推
#其本质是把test函数导入到 package 名下，用package.调用

