import threading, time

def loop():
    print(f"thread {threading.current_thread().name} starting")
    n = 0
    while n<5:
        n = n + 1
        print(f"thread {threading.current_thread().name} >>> {n}")
        time.sleep(1)
    print(f"thread {threading.current_thread().name} end")

# print(f"thread {threading.current_thread().name} thread starting") #主线程
# t = threading.Thread(target=loop, name = "LoopThread")
# t.start()
# t.join()
# print(f"thread {threading.current_thread().name} thread ended")

###################################################
""" 在多线程中各线程会共享global变量，这会导致所谓的race condition（竞态条件）即多条线程同时穿插改变量把逻辑搞乱，因为在变量操作中不是atomic operation（原子操作，瞬间完成）
    python有GIL（global interpreter lock）限制同一时间内只有单一线程执行bytecode（字节码），但是不会限制race condition
    race condition的问题可以用lock解决，其本质是给一个共享执行区域上一个锁，当某个线程在执行此部分的同时间内其他线程不能执行，直到锁被释放。通过thread.lock()实现"""

balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        # lock.acquire() #获得锁
        # try:change_it(n)
        # finally:lock.release() #松锁
        with lock:
            change_it(n) #更加优雅的写法

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

##############################################################
#threadlocal
global_dict = {}  #创建公共dict每个线程各取所需
class Student(object):
    def __init__(self, name):
        self.name = name

# def process_student(name):
#     std = Student(name)
#     global_dict[threading.current_thread()] = std
#
# def task1():
#     std = global_dict[threading.current_thread()]
#     ...
#
# def task2():
#     std = global_dict[threading.current_thread()]
#     ...

#
import threading

local_school = threading.local()#创建全局ThreadLocal对象
def process_student():
    std = local_school.student # 获取当前线程关联的student
    print(f"hello, {std.name}(in {threading.current_thread().name})!")

def process_thread(name):
    local_school.student = Student(name) # 绑定ThreadLocal的student
    process_student() #str = Student(name)

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start(), t2.start()
# t1.join()
# t2.join()









