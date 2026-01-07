# def enroll(name, gender, city = "toronto", country = "canada"):
#     print(name)
#     print(gender)
#     print(city)
#     print(country)
# enroll("Michael", "male", country = "USA")

# def add_end(L = None):
#     if L is None:
#         L = []
#     L.append('end')
#     return L

def calc(*numbers):
    # 用*在参数前面，把参数变成可变参数(variable-length)，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。可变参数会自动组装一个tuple
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(calc(1,2,3))
n1 = [1,2,3,4,5]
print(calc(*n1))
#* here mean to put all items from list into the function as variables.

def person(name, age, **kw):
    #用**在参数前，把参数变成关键词参数(keyword parameter), 自动组装一个dict
    print('name:', name, 'age:', age, 'other:', kw)

person("michael", "18", gender = "M", language = "python")

del person
def person(name, age, *, city = 'toronto', job):
    #命名关键字参数，以限制制关键字参数的名字
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)

person("michael", "18", job = "Python")

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# practise, coffee serving
def cafe(name, drink = "coffee", *, size = "medium", sugar = 0, milk = False, **kw):
    print("customer name:", name,
          "\ncustomer drink:", drink,
          "\ncustomer size:", size,
          "\ncustomize:", f"sugar: {sugar}",f"milk: {milk}")
    if kw != {}:
        print("others", kw)
    print("***************************************")

cafe("Michael")
cafe("nigga", topping = "shit")
cafe("catgirl", "iced cap", size = "small", sugar = 10, milk = True, topping = "Mic's love❤️")


def dungeon(name, weapon = "Rusty sword", armor = "Leather Armor", *item, level = 1, hp = 100, mana = 50, **status):
    print("name:", name,
          "\nweapon:", weapon,
          "\narmor:", armor)
    if item == ():
        print("no item")
        print("You venture empty-handed… brave or foolish?")
    else:
        print("item:", item)
    print("level:", level,
          "\nhp:", hp)
    if hp <= 50:
        print('Warning: fragile soul!')
    print("mana:", mana)
    if status != {}:
        print("status:", status)
    for i in status:
        if status[i] == True:
            print("dangerous effect:", i)

dungeon("Michael", "sacred dick", "light armor", level = 10, hp = 1, monster_girl_lover = True, harem_owner = True)


