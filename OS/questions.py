#3线程打印
import queue
import random
import threading
import time


def print_thread(n):
    print(f"thread {n} is running")

threads = []

# for i in range(3):
#     t = threading.Thread(target=print_thread, args=(i,))
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

##############################################################
#睡觉
def sleep():
    print(f"{threading.current_thread().name} is sleeping")
    time.sleep(1)
    print("Done")

# t = threading.Thread(target=sleep)
# t.start()
# t.join()

#############################################################
#并发线程计算level 1
def sum():
    sum = 0
    print(f"{threading.current_thread().name} is summing")
    for i in range(100):
        sum += i
    print(f"{threading.current_thread().name}: {sum}")

# thread = []
# for i in range(5):
#     t = threading.Thread(target=sum)
#     t.start()
#     thread.append(t)
#
# for i in thread:
#     i.join()

############################################################
#并发线程计算level 2
def calculate_sum(start, end):
    sum = 0
    print(f"{threading.current_thread().name} is summing")
    for i in range(start, end):
        sum += i
    print(f"{threading.current_thread().name}: {sum}")
    q.put(sum)

threads = []
Range = [(0,100), (100, 200), (200, 300)]
q = queue.Queue()
SUM = 0

# for i in range(len(Range)):
#     t = threading.Thread(target=calculate_sum, args=(Range[i][0], Range[i][1]))
#     t.start()
#     threads.append(t)
# for i in threads:
#     i.join()
# while not q.empty():
#     SUM += q.get()
#
# print(f"total sum is {SUM}")

##############################################################
#线程暴力破解, 五个线程同时破解谁先找到就停止

password = random.randint(1000, 10000)
found = threading.Event()

def FUCKPASSWORD(start, end):
    for i in range(start, end):
        if found.is_set():
            break
        if i == password:
            print(f"{threading.current_thread().name} found the password: {i}")
            found.set()
            break

threads = []
Range = [(1000,2000), (2000, 4000), (4000, 6000), (6000, 8000), (8000, 10000)]

for i in range(len(Range)):
    t = threading.Thread(target=FUCKPASSWORD, args=(Range[i][0], Range[i][1]))
    threads.append(t)
    threads.append(t)
    t.start()
for t in threads:
    t.join()



