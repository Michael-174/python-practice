#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(list(dir("ABC")))

word = "ABC"
print(len(word))
print(word.__len__()) #此两行代码等价，len function的本质就是调用其__len__方法

class word:
    def __len__(self):
        return 10000 #可以自己写类定义其len

word = word()
print(len(word))

class Myobject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x ** 2

obj = Myobject()
print(hasattr(obj, "power")) #hasattr函数会试着去取 obj.attr，看能不能成功，如果成功返回 True，报错返回 False。
print(hasattr(obj, "x"))
print(hasattr(obj, "y"))
setattr(obj, "y", 12) #显而易见setattr可以创建/修改属性
print(hasattr(obj, "y"))
print(getattr(obj, "y")) #获得属性
print(getattr(obj, "z", "nigga")) #如果找不到属性比如这里的z，可以在后面加上默认值
fn = getattr(obj, "power") #getpower还可以获取并赋值
print(fn())