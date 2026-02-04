class student(object): #定义类
    def __init__(self,name,score): #初始化方法
        self.name=name
        self.score=score

    def __str__(self): #特殊方法
        return f"name: {self.name}, score: {self.score}" #__str__是一个特殊方法，定义对象被打印时现实的内容，否则当对象被打印的时候会显示<__main__.student object at 0x000001CEC70E4C20>

    def get_grade(self): #普通方法
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"
student1 = student("Michael",99)
print(student1)
print(student1.get_grade())
#面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

class nigga_detecter(object):
    def __init__(self,answer = input("Will you say nigga? yes/no")):
        self.answer=answer
    def detect(self):
        if self.answer == "yes":
            return "you are a nigga! congrats!"
        elif self.answer == "no":
            return "you are not nigga! get out!"
person1 = nigga_detecter()
print(person1.detect())
