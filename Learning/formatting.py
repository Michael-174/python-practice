a = "Hello %s" % "World"
# print(a)

b = "hi, %s, you have $%d" % ("John", 100)
# print(b)

#   %d use for int
#   %f use for float
#   %s use for string
#   %x use for hex (16)

c = '%2d-%02d' % (3, 1)# 输出: ' 3-01'
# print(c)
d = '%.2f' % 3.1415926    # 输出: '3.14'
# print(d)

#   % [填充字符][最小宽度][.小数位数][类型]
e = "%.6s" % 3.1415926
# print(e)

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2-s1)/s1 * 100
print("%.1f" % r)
