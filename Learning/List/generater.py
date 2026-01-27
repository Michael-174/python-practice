# L1 = [x*x for x in range(10)]
# L2 = (x*x for x in range(10)) #用括号创建generator
# print(L2)
# print(next(L2)) #use next to let the generator generate next value
# print(next(L2))
# print(next(L2))
# print("********************************")
# for x in L2:
#     print(x)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# def fib(total):
#     fibonacci = [0, 1]
#     if total <= 2:
#         return fibonacci[:total]
#     for i in range(total-2):
#         fibonacci.append(fibonacci[-1] + fibonacci[-2])
#     return fibonacci
#
# while True:
#     try:
#         t = int(input("enter number to create fibonacci sequence: "))
#         if t < 0:
#             print("please enter a non-negative integer")
#             continue
#         break
#     except ValueError:
#         print("invalid input, please try again")
#
# print(fib(t))

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done' #如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# g = fib(6)
# while True:
#     try:
#        x = next(g)
#        print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break #试图显示return值

# def odd():
#     print("step 1")
#     yield 1
#     print("step 2")
#     yield 2
#     print("step 3")
#     yield 3
# o = odd()
# print(next(o))
# print(next(o))

#杨辉三角
def Ytrangle(max):
    n, a, b = 0, 1, 1
    level = [a]
    while n < max:
        yield level
        a = level.copy()
        a.append(b)
        for i in range(1, len(level)):
            a[i] = level[i-1] + level[i]
        level = a.copy()
        n = n + 1

for i in Ytrangle(100):
    print(i)


