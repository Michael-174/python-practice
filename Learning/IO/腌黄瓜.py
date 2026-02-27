import pickle
d = dict(name = "Michael", age = 24, height = 70)
print(pickle.dumps(d)) #把d编码成二进制然后打印出来

with open("dump.pkl", "wb") as f:
    pickle.dump(d, f) #把二进制“倒”进文件里存起来
with open("dump.pkl", "rb") as f:
    d = pickle.load(f) #把文件取出来
print(d)