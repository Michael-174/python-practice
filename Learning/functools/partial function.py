print(int("12345"))
print(int("12345", 16)) #int可以接受参数base，将括号里的数字看作是base数，然后转换为base 10

def int2(x, base=2):
    return int(x, base)
print(int2("1111"))
#默认从二进制转换
print(int2("1111", 2))

import functools
int2 = functools.partial(int, base=2)
#可以用functool的偏函数设定默认值，再返回一个新函数

print(int2('10010'))
# kw = {'base': 2}
# print(int2("1111", **kw)) #相当于上面

max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
print(max2(max2(5, 6, 7))) #相当于：
# args = (10, 5, 6, 7)
# max(*args)
