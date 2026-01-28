#，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
    return x % 2 == 1

a = list(filter(is_odd, range(1, 10)))
#在这里1，3，5，7，9符合is_odd，所以被保留了
print(a)

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

if 2>1 and 3>1:
    print(2)