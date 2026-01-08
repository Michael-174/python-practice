# class People:
#
#     def __init__(self, name):
#       self.name = name
#     def nameprint(self):
#         print(self.name)
#
# person1 = People("Sally")
# person2 = People("Louise")
# person1.nameprint()

# add_19 = lambda x: x + 19
# print(add_19(19))
#
# numbers = [1, 12, 13, 4]
# def foo(bar):
#     aug = str(bar) + "street"
#     return aug
#
# for item in numbers:
#     print(foo(item))
#
# def sayHello():
#     print('Hello World!')
# sayHello()
# sayHello()

# class employee:
#     def __init__(self, hour, sale):
#         self.hour = hour
#         self.sale = sale
#     def earning(self):
#         if self.sale > 1000:
#             print("this employee has earned $%.1f" % (35*self.hour+0.1*self.sale))
#         else:
#             print("this employee has earned $%.1f" % (35*self.hour))
#
# employee1 = employee(160, 15040)
# employee1.earning()
# #this employee has earned $7104.0

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle area ({self.width*self.height})"

rectangle = Rectangle(10, 10)
print(rectangle)

