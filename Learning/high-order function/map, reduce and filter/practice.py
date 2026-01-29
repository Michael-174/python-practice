#从 1 到 150 的数字里，筛选出能被 3 整除的数字, 对筛出来的数字求平方, 求这些平方的和
# def divide3(x):
#     return x % 3 == 0
# def square(x):
#     return x ** 2
# def program(x):
#     result = list(filter(divide3, x))
#     result = map(square, result)
#     result = sum(result)
#     return result
# a = program(range(1, 150))
# print(a)

#筛选出首字母和尾字母相同的单词，将它们全部转换为大写，用 reduce 拼接成一个字符串
from functools import reduce
words = ["apple", "level", "banana", "radar", "grape", "civic"]
def condition(x):
    return x == x[::-1]
def upper(x):
    return x.upper()
def combine(x, y):
    return x + y
def program(x):
    x = filter(condition, x)
    x = map(upper, x)
    x = reduce(combine, x)
    return x
print(program(words))

#无限奇数平方生成器
def numbers():
    n = 1
    while True:
        yield n
        n = n + 2
def square(x):
    return x ** 2
def generator():
    it = numbers()
    it = map(square, it)
    return it

g = generator()
for x in range(20):
    print(next(g))














