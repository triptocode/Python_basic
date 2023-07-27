### 프로세스 간의 객체 공유: Queue() 클래스
# 큐의 특징: 데이터가 몇개 남았는지 카운터가 동작함.

# # ---------------------------------------------------- Queue 예제1 : 첫버째 방식 -------------------------------------------------------
# from multiprocessing import Queue, Process
# import time

# def pro1(q): #q객체에 데이터를 넣는다 
#     for i in range(30): # 0부터 29까지 
#         q.put(i) # 데이터를 입력하는 메서드
#         print("p1: sleep for 0.5sec")  # ( 내가 추가한 코드 )
#         time.sleep(0.5)
# def pro2(q):
#     items = [] # empty list 
#     while True: #무한루프, while 1 과 동일
#         item = q.get() # q에 있는 데이터를 가지고 옴
#         items.append(item)
#         print(f"p2: p객체에서 {item}를 가지고 왔다.")
#         print(f"현재 q에 저장된 값은 {items}입니다.")

# # main code 
# if __name__=="__main__":

#     queue = Queue() # 데이터를 공유할 큐 객체 생성

#     p1 = Process(target=pro1, args=(queue,)) # 반점,  꼭 표시! 튜플 군집형태로 넘겨주기 위함
#     p2 = Process(target=pro2, args=(queue,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()



#  ----------------------------------------------------- Queue 예제2 : 두번째 방식 -----------------------------------------------------
from multiprocessing import Queue, Process
import time

def pro1(q): #q객체에 데이터를 넣는다 
    for i in range(30): # 0부터 29까지 
        q.put(i) # 데이터를 입력하는 메서드
        print("p1: sleep for 0.5sec")  # ( 내가 추가한 코드 )
        time.sleep(0.5)
def pro2(q):
    items = [] # empty list 
    while True: #무한루프, while 1 과 동일
        item = q.get() # q에 있는 데이터를 가지고 옴
        items.append(item)

        #  예제1 과 다른부분 - 2곳 : 추가된 코드 1
        if item is None: # null과 비슷
            print("모든 데이터를 가지고 왔습니다. \n")
            break

        print(f"p2: p객체에서 {item}를 가지고 왔다.")
        print(f"현재 q에 저장된 값은 {items}입니다.")

# main code 
if __name__=="__main__":

    queue = Queue() # 데이터를 공유할 큐 객체 생성

    p1 = Process(target=pro1, args=(queue,)) # 반점,  꼭 표시! 튜플 군집형태로 넘겨주기 위함
    p2 = Process(target=pro2, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None) #  예제1 과 다른부분 - 2곳 : 추가된 코드 2  // #p1이 끝날때 까지 기다렸다가 None 값을 입력   
    p2.join()

    p1.terminate()  # terminate() 안넣어도 프로세스 작동하지만, 종료가 안될수이어 강제종료해주기 위함
    p2.terminate()
    

## 설명: 프로세스 간 통신을 위해 multiprocessing.Queue를 사용
# 하위 프로세스인  pro2가 q.get()메서드 호출하여 q에서 데이터를 
# 가져오기 위해 대기함 --> 프로세스가 종료 되지 않는 문제가 발생 
