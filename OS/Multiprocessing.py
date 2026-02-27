import os
from multiprocessing import Process

def run_proc(name):
    a = int(name)*10
    print(f"run child process {name}, {os.getpid()}, result: {a}")

# if __name__ == '__main__':
#     print(f"Parent process {os.getpid()}")
#     p = Process(target=run_proc, args=(1,))
#     print("child process start")
#     p.start() #子进程开始执行
#     p.join() #让主进程等子进程执行完，执行完再继续
#     print("child process done")

#####################################################################
#pool

import os, time, random
from multiprocessing import Pool

def long_time_task(name):
    print(f"Run task {name} {os.getpid()}")
    print("#################################")
    start = time.time() #获取当前时间
    time.sleep(random.random()*3) #睡几秒的觉
    end = time.time()
    print(f"{name} took {(end - start):.2f} seconds") #.2f, 保留两位小数

# if __name__ == '__main__':
#     print(f"Parent process {os.getpid()} starting")
#     p = Pool(3)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,)) #异步提交任务
#     print("Waiting for all subprocesses done...")
#     p.close()
#     p.join()
#     print("All subprocesses done.")

###################################################################
#subprocess

import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org']) #让操作系统开一个新的进程，命令是 nslookup www.python.org
# print('Exit code:', r)

# r = subprocess.call("dir", shell=True) #调用cmd，让进程去查dir

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)