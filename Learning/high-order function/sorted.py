#用sorted函数可以排序list或任何序列，其核心是比较两个元素的大小

random = [12,-15,2,0,67,-45]
random = sorted(random)
print(random) #默认sorted会从小到大排序

random = sorted(random, reverse=True)
print(random) #从大到小

random = sorted(random, key=abs)
print(random) #按照绝对值排序

#ASCII order: number < lower case < upper case

random_str = ["a", "A", "Z", "Ab", "cAoNima", "nigga"]
random_str = sorted(random_str, key = str.lower)
print(random_str) #把所有项都变成小写后比较

#问题：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0] #用每个tuple的第一个元素“xxx”排序
L = sorted(L, key = by_name)
def by_score(t):
    return t[1] #用每个tuple的第二个元素 数字 排序
L = sorted(L, key = by_score)
print(L)