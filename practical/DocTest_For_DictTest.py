from practical.DictTest import Dict

#doctest其本质是模拟其python shell来确定引用及其输出结果是否一致
class DictTest(dict):
    #用>>>加表达式，然后下一行是输出结果
    """
    Simple dict but also support access as x.y style.
    >>> d = Dict(name="Alice", age = 18)
    >>> d.age
    18

    >>> d["age"]
    18
    """
    def __init__(self, **kw):
        super(DictTest, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest
    doctest.testmod()

