#StringIO
from io import StringIO
f = StringIO()
f.write('Hello, Michael!')
print(f.write('Hello, Michael!')) #会打印字符数量

f1 = StringIO("Hello!\nNigga!\nGoodbye!")
# while True:
#     s = f1.readline()
#     if  s == '':
#         break
#     print(s.strip())
#或
# for line in f1.readlines():
    # print(line.strip())

#############################################################
#BytesIO
from io import BytesIO
f2 = BytesIO()
print(f2.write("中文".encode('utf-8')))
print(f2.getvalue())



