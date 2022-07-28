import os, random
from multiprocessing import Process, Pipe

def producer_task(conn):
    value = random.randint(1, 10)
    conn.send(value) # 메인 함수에 구현된 connect 객체의 send 함수를 통해 메인함수로 값을 전달한다. 
    print(f'Value {value} send by PID {os.getpid()}') # os 모듈은 프로세스의 id를 얻게 해준다.
    conn.close() # 항상 끝나면 close를 통해 연결을 끊어준다.

def consumer_task(conn):
    print()
    print(f'Value {conn.recv()} send by PID {os.getpid()}')

if __name__ == '__main__':
    print(__name__)
    producer_conn, consumer_conn = Pipe()
    consumer = Process(target=consumer_task, args=(consumer_conn,))
    producer = Process(target=producer_task, args=(producer_conn,))

    consumer.start()
    producer.start()

    consumer.join()
    producer.join()
    
