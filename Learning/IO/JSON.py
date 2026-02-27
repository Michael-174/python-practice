import json
d = dict(name = "Michael", age = 24, height = 70, weight = 80)
# print(json.dumps(d)) #把d变成json

#################################################################

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def student2dict(student):
    return {
        "name": student.name,
        "age": student.age
    }

def dict2student(d):
    return Student(d["name"], d["age"])

s = Student("Michael", 24)
# print(json.dumps(s, default=student2dict)) #可以用转换函数把类转换成dict
jstr = json.dumps(s, default = lambda obj: obj.__dict__, indent = 4)
print(json.loads(jstr, object_hook = dict2student)) #用dict2student反序列化成一个student对象实例


#########################################################
class Student1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def dict(self):
        return dict(name="nigga", age=100)

s1 = Student1("Michael", 24)
# print(json.dumps(s1.dict())) #直接加字典也行

