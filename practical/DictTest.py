d = dict(name = "Michael", age = 18) #正常用dict
# print(d)

class Dict(dict): #此类可以用Dict替代内置类dict，从而实现把[xxx]等价与属性调用
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("no such attribute")
    def __setattr__(self, item, value):
        self[item] = value

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# d = Dict()
# print(d.age)
# print(d["age"]) #两者等价且都可使用