class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal): #以animal继承，dog可以沿用animal的方法
    def run(self):
        print('Dog is running...') #当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
    # pass
dog = Dog()
dog.run()
print(type(Animal))
print(type(dog))

a = list()
b = Animal()
print(isinstance(b,Animal)) #结果是True因为当我们定义一个class的时候，我们实际上就定义了一种数据类型。
c = Dog()
print(isinstance(c,Animal)) #c既是Dog又是Animal，因为Dog是从Animal继承下来的

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Dog()) #对于一个变量，我们只需要知道它是animal类，就可以调用方法。可以修改子类型而无需修改run_twice

class Running():
    def __init__(self, obj):
        self.obj = obj
    def run(self):
        print(f"{self.obj} is running...")

class Nigga_running(Running):
    pass
nigga = Nigga_running("nigga")
nigga.run()



