import threading
import logging
from queue import Queue
import time 

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

channel = logging.StreamHandler()
channel.setLevel(logging.DEBUG)
channel.setFormatter(formatter)
logger.addHandler(channel)

fibo_dict = {}
shared_queue = Queue() # 데이터를 공유할 containor
num_list = [3, 10, 5, 7]
queue_condition = threading.Condition() # 자원에 접근할 때 작업들을 동기화하려는 목적

def fibonacci_task(condition):
    with condition: # with 문이 없으면 lock 취득과 해제를 명시해야 한다. 
        while shared_queue.empty(): # 큐에 원소가 들어올 때 까지 기다린다. 
            logger.info("[%s] - wating for elements in queue..." % threading.current_thread().name)
            time.sleep(1)
            condition.wait()
        else:
            value = shared_queue.get() # 큐에 들어온 데이터를 하나 가져온다. 큐는 FIFO임을 생각. 
            logger.info(f"[{threading.current_thread().name}] - The input value {value} is gotten from the queue.")
            a, b, = 0, 1
            for item in range(value):
                a, b = b, a + b
                fibo_dict[value] = a
        shared_queue.task_done() # 큐에 테스크의 종료를 알린다. 
        logger.debug("[%s] - Result %s" % (threading.current_thread().name, fibo_dict))
        time.sleep(1)

def queue_task(condition, item_lst):
    logging.debug('Starting queue_task...')
    with condition:
        for item in item_lst:
            shared_queue.put(item)
        logging.debug("Notifying fibonacci_task threads that the queue is ready to consume...")
        condition.notifyAll() # 각 스레드에 큐를 사용할 준비가 됐다고 알린다. 

# 각 작업을 위한 스레드들을 정의한다. 
# 스레드 클래스의 생성자에서 target인자에 함수명을 입력한다.
threads = [threading.Thread(daemon=True, target=fibonacci_task, args=(queue_condition,)) for i in range(4)]
# 스레드 생성을 실행해서 대기시킨다. 
[thread.start() for thread in threads]

# queue_task 함수를 스레드에 할당하고 실행시켜서 shared_queue를 채운다. 
prod = threading.Thread(name='queue_task_thread', daemon=True, target=queue_task, args=(queue_condition,num_list))
prod.start()

# 부모 스레드를 끝까지 진행하지 않고 자식 스레드들이 종료될 때까지 기다린다. 
[thread.join() for thread in threads]


# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a


# for i in range(1, 10):
#     print(fibonacci(i))

# num_list = []
