class student:
    pass

s = student()
s.name = "nigga"
print(s.name)

def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) #动态给实例绑定方法，这只适用于单一实例
s.set_age(100)
print(s.age)

def set_score(self, score):
    self.score = score
student.set_score = set_score #可以把方法定义绑定给类，这样所有此类的实例都可以用
s.set_score(111)
print(s.score)

#__slots__可以限制实例可以添加的属性，写在定义类的时候
class Student(object):
    __slots__ = ('name', 'age')
s = Student()
s.name = "Rose"
s.age = 20
s.score = 100 #在这里定义score attr会报错
#注意, __slots__对继承的类无效
