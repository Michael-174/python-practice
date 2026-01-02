a = int(input("hours:"))
b = float(input("rate:"))

def pay(x,y):
    if x > 40:
        return 40*y+(x-40)*(1.5*y)
    else:
        return x*y

print("your pay is", pay(a,b))
