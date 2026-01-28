#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections.abc import Iterator
a = isinstance((x for x in range(10)), Iterator)
print(a)
#可以用iter把list，tuple等iterable 转换成 iterator
b = isinstance(iter([]), Iterator)
print(b)

it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
#9-14 equal to for loop below
for x in it:
    pass
