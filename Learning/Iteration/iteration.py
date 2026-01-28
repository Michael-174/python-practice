test = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

for iteration in enumerate(test.items()):
    print(iteration) #enumerate出tuple来遍历
for x,y in enumerate(test.items()):
    print(x,y) #如果给enumerate 两个值， 第一个会变成序号，第二个是遍历
# for iteration in test.items():
#     print(iteration) #普通迭代，没有序号

from collections.abc import Iterable
a = isinstance(test, Iterable) #检查dict test是不是可迭代
if a:
    print(f"{test} is an iterable")