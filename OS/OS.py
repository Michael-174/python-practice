import os
# print(os.name) #输出NT表示老子再用shit windows
# os.uname() #在windows上不提供
# print(os.environ)

# print(os.environ.get("PATH"))

# print(os.path.abspath('.'))
a = os.path.join('/Users/dazhe.DESKTOP-PCQFD5L/PyCharmMiscProject', 'testdir') #把两段路径合成在一起
a = os.path.split(a) #把路径拆分出来，总是拆最后的路径
a = os.path.join(*a)
# print(a)
os.mkdir(a) #创建目录(如果存在就会报错)
os.rmdir(a) #删除空目录(如果不存在就会报错)

#############################################################

b = r"C:\Users\dazhe.DESKTOP-PCQFD5L\PyCharmMiscProject\Learning\IO\test.txt"
txt = os.path.splitext(b)
# print(txt[1])
os.rename(b, "../Learning/IO/test.txt")

#############################################################
print([x for x in os.listdir('.') if os.path.isdir(x)]) #找到当前目录的全部文件夹
print(os.getcwd()) #打印当前文件的位置

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']) #找到当前目录的全部python文件
