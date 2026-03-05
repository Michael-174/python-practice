import multiprocessing
from random import randrange

# a = randrange(1000, 10000)
# print(f"pass word hidden: {a}")

# def breaker(n):
#     for i in range(1000, 10000):
#         if i == n:
#             print(f"password breaks! password is {i}")
#             break
# breaker(a)

#############################################################
import multiprocessing
from random import randrange
import os
from multiprocessing import Pool, Event, Queue, Process

a = randrange(1000, 10000)
print(f"pass word hidden: {a}")

def breaker0(password, queue):
    for i in range(1000, 2500):
        if password == i:
            queue.put(i)
            print(f"password found: {i}, process id: {os.getpid()}")
            break
def breaker1(password, queue):
    for i in range(2500, 5000):
        if password == i:
            queue.put(i)
            print(f"password found: {i}, process id: {os.getpid()}")
            break
def breaker2(password, queue):
    for i in range(5000, 7500):
        if password == i:
            queue.put(i)
            print(f"password found: {i}, process id: {os.getpid()}")
            break
def breaker3(password, queue):
    for i in range(7500, 10000):
        if password == i:
            queue.put(i)
            print(f"password found: {i}, process id: {os.getpid()}")
            break
if __name__ == '__main__':
    q = Queue()
    flag = Event()
    pool = Pool(multiprocessing.cpu_count())
    pool.apply_async(breaker0, args=(a,q))
    pool.apply_async(breaker1, args=(a,q))
    pool.apply_async(breaker2, args=(a,q))
    pool.apply_async(breaker3, args=(a,q))
    if not q.empty():
        result = q.get()
        flag.set()
        print(result)






