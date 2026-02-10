class Student(object):

    def __init__(self, name, score): #如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('score must be between 0 and 100')
        self.__score = score

    def get_score(self): #如果要得到private，要自己定义此方程
        return self.__score
Michael = Student("Michael",99)
# print(Michael.__score) #从这边无法访问__score，因为python把它改名了
print("强行访问 score:",Michael._Student__score) #用改名之后的名字还是可以访问的
Michael.score = 60
print(Michael.score)
setattr(Michael, "score", 90) #setattr 用字符串“创建 or 修改”对象的属性。在这里因为score被私有化了，setattr创了一个新attribute “score”
print(Michael.score)
Michael.set_score(100)
print(Michael.get_score())
print(getattr(Michael, "score"))
print()

