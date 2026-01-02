x = 3

def func(a):
    return lambda x: x*a

f = func(x)

print(f(x))

