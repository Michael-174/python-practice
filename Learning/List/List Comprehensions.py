# a = [a * a for a in range(1,40) if a % 2 == 0]
# print(a) #循环生成偶数幂

# b = [m+n for m in "nigga" for n in "nigga"]
# print(b) #二层循环声称list

# c = {"a":1, "b":2, "c":3, "d":4, "e":5}
# c = [f"{x} = {y}"for x,y in c.items()]
# print(c) #循环打印dict

# import os
# scan = [x for x in os.listdir('.')]
# print(scan)

# Capital = ["A", "B", "C", "D", "E", "F"]
# Not_Capital = [a.lower() for a in Capital]
# print(Not_Capital)

# a = "nigga"
#
# if isinstance(a, str): #use isinstance to check type
#     print(f"{a} is a string")
#
# L2 期待输出: ['hello', 'world', 'apple']
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [a for a in L1 if isinstance(a, str)]
print(L2)