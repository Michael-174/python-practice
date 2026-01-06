# class myclass:
#     x = 5
#
# p1 = myclass()
# print(p1.x)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"{self.name}({self.age})"
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = person("Yara", 16)
# print(p1.name)
# print(p1.age)

p1.age = 40
print(p1.age)

del p1.age

print(p1)

p1.myfunc()
