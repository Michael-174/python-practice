# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# 普通递归

def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
# 尾递归，reduce stack overflow but not optimized in python
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。

print(fact(5))

# def move(n, a, b, c):
#     if n == 1:
#         print(f"move disk{1} from a to b")
#         return
#     move(n - 1, a, c, b)
#     print(f"move disk{n} from a to c")
#     move(n - 1, b, a, c)
# move(5, "A", "B", "C")



