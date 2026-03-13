#Test slave

import time, sys,queue
from multiprocessing.managers import BaseManager

class Nigga(BaseManager):
    pass

Nigga.register('get_task_queue')
Nigga.register('get_result_queue')

server_addr = "127.0.0.1"
m = Nigga(address=(server_addr, 5000), authkey=b'slavery')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout = 1)
        print(f"run task {n*n}")
        r = f"{n} x {n} = {n*n}"
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print("task queue is empty")
print("slave exit, watermelon feed required.")
