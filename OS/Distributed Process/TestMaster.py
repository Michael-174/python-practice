#test master
import random, queue, time
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class NiggaManager(BaseManager): pass #创建一个空方法继承自BaseManager，不动它的基础功能

def get_task_queue(): #任务
    return task_queue
def get_result_queue(): #结果
    return result_queue

if __name__ == '__main__':
    NiggaManager.register('get_task_queue', callable=get_task_queue) #注册队列给Queuemanager管理
    NiggaManager.register('get_result_queue', callable=get_result_queue) #同上

    manager = NiggaManager(address=('127.0.0.1', 5000), authkey=b'slavery') #
    manager.start() #工厂开门，让老子的奴隶们上班
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        #生成一个随机数然后把其放进queue task里面让slaves可以拿
        n = random.randint(0, 10000)
        print(f"put task {n}")
        task.put(n)
    print("try get results...")
    for i in range(10):
        r = result.get(timeout=10)
        print(f"get result: {r}")

    manager.shutdown()
    print("master exit")


