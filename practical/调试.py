def nig1():
    n = int(input("enter the number"))
    assert n!= 0, "n is 0!" #使用assert 来debug，assert之后的表达式必须为true，否则会以之后的str报错
    n = int(10/n)
    print(n)
# nig()

def nig2(a,b):
    a = int(a)
    b = int(b)
    print(a/b)

# nig2(10,0)

################################################################################################
#logging
import logging
logging.basicConfig(level=logging.DEBUG)

def nig3(a, b):
    logging.debug(f"a = {a}")
    logging.debug(f"b = {b}")

    try:
        a = int(a)
        b = int(b)
        print(a / b)
    except Exception as e:
        logging.error(f"Error: {e}")

nig3(10, 0)
