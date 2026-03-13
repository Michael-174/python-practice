import multiprocessing
from random import randrange, randint

# a = randrange(1000, 10000)
# print(f"pass word hidden: {a}")

# def breaker(n):
#     for i in range(1000, 10000):
#         if i == n:
#             print(f"password breaks! password is {i}")
#             break
# breaker(a)

#############################################################
#暴力破解
import multiprocessing
from random import randrange
import os
from multiprocessing import Process, Queue, Event



# worker函数
# def worker(password, start, end, queue):
#     for i in range(start, end):
#
#         if password == i:
#             print("password found:", i, "pid:", os.getpid())
#             queue.put(i)
#             break
#
# if __name__ == "__main__":
#
#     # 随机密码
#     password = randrange(1000, 10000)
#     print("password hidden:", password)
#
#     queue = Queue()
#     ranges = [
#         (1000,2500),
#         (2500,5000),
#         (5000,7500),
#         (7500,10000)
#     ]
#
#     processes = []
#
#     # 创建并启动 worker
#     for r in ranges:
#         p = Process(target=worker,
#                     args=(password, r[0], r[1], queue))
#         p.start()
#         processes.append(p)
#
#     # ⭐ 关键点：主进程阻塞等待结果
#     result = queue.get()
#
#     print("Solved password:", result)
#
#     # 等待所有进程结束
#     for p in processes:
#         p.join()


###################################################################
#gamble破解
def hakari(password, start, end, queue, event):
    while not event.is_set():
        i = randint(start, end)
        if i == password:
            print("password found:", i, "pid:", os.getpid())
            queue.put(i)
            event.set()
            break

if __name__ == '__main__':
    event = Event()
    password = randrange(1000, 10000)
    print("password hidden:", password)
    queue = Queue()
    ranges = [
        (1000, 2500),
        (2500, 5000),
        (5000, 7500),
        (7500, 10000)
    ]
    processes = []
    for r in ranges:
        p = Process(target=hakari,
                    args=(password, r[0], r[1], queue, event))
        p.start()
        processes.append(p)

    result = queue.get()
    print("Solved password:", result)
    for p in processes:
        p.join()





