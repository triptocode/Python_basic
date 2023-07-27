##### 프로세스 간의 객체(데이터) 공유: simpleQueue 클래스

from multiprocessing import SimpleQueue, Process
import time

#
def pro1(sq):
    for i in range(10):
        sq.put(i)
        print(f"P1: simpleQue에 {i}를 담았습니다.")
        time.sleep(0.5)

#심플큐에 

def pro2(sq):
    items = []
    while True:
        item =sq.get()
        if item is None:
            print(f"P2: simpleQue의 내용을 모두 가져왔습니다. 끝")  
            break
        print(f"P2: simpleQue의 값:{item}")
        items.append(item) #리스트에 가져온 값 추가됨. 

#main코드 부분
if __name__=="__main__":
    squeue = SimpleQueue() ## 데이터 공유를 위한 심플큐 객체 생성
    p1 = Process(target =pro1, args=(squeue,))
    p2 = Process(target =pro2, args=(squeue,))

    p1.start()
    p2.start()

    p1.join()
    squeue.put(None)
    p2.join()