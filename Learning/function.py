# def nigga(n):
#     return "nigga"
# from function import nigga
# print(nigga(1))
#
# def nothing(): #空函数
#     pass
# print(nothing())

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('stupid nigga enter a number!')
#     if x >= 0:
#         return x
#     else:
#         return -x
##isinstance, check if x is a certain datatype or not
# print(my_abs("a"))

##question, define a function that return a quadratic equation
import math
def quadratic(a, b, c):
    check = b ** 2 - 4 * a * c
    if check < 0:
        return "no real number solution"
    x1 = (-b + math.sqrt(check))/(2*a)
    x2 = (-b - math.sqrt(check))/(2*a)
    if x1 == x2:
        return x1
    return round(x1, 2), round(x2, 2)
a = float(input("Enter equation a: "))
b = float(input("Enter equation b: "))
c = float(input("Enter equation c: "))
print(quadratic(a, b, c))


