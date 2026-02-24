#对函数fact(n)编写doctest并执行：

def fact(n):
    """
    >>> fact(1)
    1
    >>> fact(5)
    120
    >>> fact(-1)
    Traceback (most recent call last):
    ValueError
    """
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# print(fact(5))