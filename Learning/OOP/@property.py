class student(object):

    @property #@property会把此方法变成只读状态，使得用户只能通过score.setter来访问
    def score(self):
        return self._score

    @score.setter
    def score(self,score):  #用来限制_score的范围
        if not isinstance(score,int):
            raise TypeError('score must be an integer')
        if score < 0 or score > 100:
            raise ValueError('score must be between 0 and 100')
        self._score = score

    @property #@property还可以锁定那些不需要改的属性，比如grade可以直接根据score算出来A，B，或C
    def grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'

s = student()
s.score = 1
print(s.score)
print(s.grade)
#注意，property要用私有变量即self._xxx,否则会超载

##########################################################################################
#练习：请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        if not isinstance(width,int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self._width = width

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self,length):
        if not isinstance(length,int):
            raise TypeError('length must be an integer')
        if length < 0:
            raise ValueError('length must be >= 0')
        self._length = length

    @property
    def resolution(self):
        resolution = self.width * self.length
        return f"resolution is {resolution}, {self.width}x{self.length}"

my_laptop = Screen()
my_laptop.width = 1080
my_laptop.length = 1920
print(my_laptop.resolution)

