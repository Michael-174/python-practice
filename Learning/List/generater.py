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

def fib(total):
    fibonacci = [0, 1]
    if total <= 2:
        return fibonacci[:total]
    for i in range(total-2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

while True:
    try:
        t = int(input("enter number to create fibonacci sequence: "))
        if t < 0:
            print("please enter a non-negative integer")
            continue
        break
    except ValueError:
        print("invalid input, please try again")

print(fib(t))




