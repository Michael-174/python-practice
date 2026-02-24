#读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

# 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程
# 序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系
# 统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

# f = open("test.txt", 'r')
# print(f.read())
# f.close()

# try:
#     f = open("test.txt", 'r') #‘r’是默认
#     print(f.read())
# finally:
#     if f:
#         f.close() #保证无论如何都正确关闭文件

with open("test.txt") as f:
    for line in f:
        print(line)

