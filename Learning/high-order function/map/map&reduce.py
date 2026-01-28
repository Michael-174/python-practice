from functools import reduce


# def f(x):
#     return x**2

# test = [1,2,3,4,5,6,7,8,9,10]
# a = map(f, test)
# print(a) #只能显示a的object
# a = list(a)
# print(a)
#map函数三个字，函传代

# a = map(str, test)
# a = list(a)
# print(a)

# def g(x, y):
#     return x + y
# b = reduce(g, test)
# print(b)
#reduce函数三个字，函叠代： 2个参数，用结果和第三个参数计算

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# L1 = ['adam', 'LISA', 'barT']
# def normalize(name):
#     name = name.lower()
#     name = list(name)
#     name[0] = name[0].upper()
#     name = ''.join(name)
#     return name
# L2 = list(map(normalize, L1))
# print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# def fprod(l):
#     return reduce(product, l)
# def product(a,b):
#     return a*b
# print('3 * 5 * 7 * 9 =', fprod([3, 5, 7, 9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(s):
#     cut = s.split(".")
#     integer = cut[0]
#     decimal = cut[1]
#     chart = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
#     def chart2num(x, y):
#         return 10*x + y
#     def str2chart(s):
#         return chart[s]
#     return reduce(chart2num, map(str2chart, integer)) + reduce(chart2num, map(str2chart, decimal))/(10**len(decimal))
# print('str2float(\'123.4567\') =', str2float('123.4567'))



