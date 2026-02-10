class student(object):
    def __init__(self, name, age):
        self.name = name

s = student("John", 25)
print(s.name)
s.score = 100
print(s.score)

class student(object):
    name = "John" #类属性，归Student类所有
s = student()
print(s.name)
print(student.name)

s.name = "Michael"
print(s.name) #由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(student.name) #但是类属性并未消失，用Student.name仍然可以访问
del s.name
print(s.name) #即使删除s类的name atr，实例s的attr会去student查找并返回John

