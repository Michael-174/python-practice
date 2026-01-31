草泥马 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(草泥马)

def build(x, y):
    return lambda: x * x + y * y #可以把兰博作为返回值返回, 返回后是一个返回函数
print(build(1, 2))
print(build(1, 2)())