class Animal:
    def __init__(self):
        print("this is an animal")

class Mammal(Animal):
    def __init__(self):
        super().__init__()   # 调用父类构造函数
        print("this is a mammal")

class Runnable(Animal):
    def run(self):
        print("running")

class Flyable(Animal):
    def fly(self):
        print("flying")

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

dog = Dog()
dog.run()
# 输出:
# this is an animal
# this is a mammal
# running

bat = Bat()
bat.fly()
# 输出:
# this is an animal
# this is a mammal
# flying







