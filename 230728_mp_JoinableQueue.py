# from multiprocessing import Queue, Process  # 이렇게넣으면 multiprocessing.JoinableQueue() 를사용이 안됨 
import multiprocessing
from time import sleep

## JoinableQueue() 클래스란?
# multiprocessing 의 Queue 안에 내장됨 
# 프로세스간 데이터를공유 
# 카운터가 없기에, 작업이 끝났음을알려주는 task_done()이 필요함

def pro1(jq, pn):
    for i in range(10):  # 0부터 9까지
        jq.put(i)
        print(f"jq 자체를 출력:{jq}") # jq란?:<multiprocessing.queues.JoinableQueue object at 0x000001A7BEB77050>
        print(f"{pn}: jq에 값 {i}를 입력했습니다")
        sleep(0.5)  #  time.sleep() 대신 sleep() 쓰려면 위처럼 from time import sleep 를 넣어준다. 

def pro2(jq, pn):
    items = []
    while True:
        item = jq.get()
        if item is None:
            print("모든 jq객체의 데이터를 가져왔습니다.")
            break  
        items.append(item)
        print(f"{pn}: jq객체로 부터{item}을가져왔습니다.")
    print(items)
    jq.task_done() # JoinableQueue 는 카운카가 없으므로 작업의종료를 알려주어야함

a ,b = 0,1

if __name__ == "__main__":
    jqueue = multiprocessing.JoinableQueue()

    p1= multiprocessing.Process(target=pro1, args=(jqueue, a))# 함수명 , 함수의 매개변수
    p2= multiprocessing.Process(target=pro2, args=(jqueue, b))

    p1.start()
    p2.start()

    p1.join()
    jqueue.put(None) 
    p2.join()




