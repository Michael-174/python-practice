#，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
    return x % 2 == 1

a = list(filter(is_odd, range(1, 10)))
#在这里1，3，5，7，9符合is_odd，所以被保留了
# print(a)

def not_empty(s):
    return s and s.strip() #if left side is falsy, then left, else right side
#truthy(真值)：任何不为0的数，不空的序列
#falsy(假植)：int 0, float 0.0, complex 0j, empty sequence, none and false.
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
#if the value return by not_empty is falsy, then the filter will filter it out


def _odd_iter(): #这是一个奇数生成器，并且是一个无限序列。
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n): #筛选函数
    return lambda x: x % n != 0 #把n的倍数筛掉，因为倍数是0，在这里是false
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
    if n<1000:
        print(n)
    else:
        break


#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数
# 0-9 都是 回数
#非回数如何确定？首尾不同，然后首尾下一位不同。。。。。。
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
nums = range(1, 1000)
palindromes = list(filter(is_palindrome, nums))
# print(palindromes)





