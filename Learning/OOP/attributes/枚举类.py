from enum import Enum, unique
Month = Enum('Month', ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
#现在每一个month都是个实例，这就是month的枚举类
# print(Month) #显示是enum类
# print(Month.Jan)

# for name, member in Month.__members__.items():
#     print(member.value, member)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Sun)
print(Weekday.Sun.value)
for name, member in Weekday.__members__.items():
    print(member.value, member)


