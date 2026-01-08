#extend, to add something after a list
#index, to find the order of an element in a list
#pop, to remove the element on certain index
#   |if no index is given, then print the last element of the list
# numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(numbers1.index(3))
# x = numbers1.pop(2)
# print("number poped: ", x)
# numbers1.insert(2,x)
# print(numbers1)
# numbers2.insert(0,numbers1)
# print(numbers2)
# print(numbers2.index(numbers1))
# print(numbers2[0].index(3))
#
# print(sum(numbers1)/len(numbers1))
#
# #Split breaks a string into parts and produces a list of string
# a = "nigga sybau"
# b = a.split()
# print(b)
# nigga =list(a[:5])
# print(nigga)

a = [x*x for x in range(1,100) if x % 2 == 0]
print(a)
b = [m+n for m in "nigga" for n in "nigga"]
print(b)

c = {"a":1, "b":2, "c":3, "d":4, "e":5}
c = [f"{x} = {y}"for x,y in c.items()]
print(c)


