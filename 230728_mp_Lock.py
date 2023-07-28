# --------------------------------------- 예제 : lock 을 넣고 해보자 -----------------


# import multiprocessing
# import time

# #  lock을 acquire 하면 해당 쓰레드만 공유 데이터에 접근할 수 있고, 
# # lock을 release 해야만 다른 쓰레드에서 공유 데이터에 접근할 수 있습니다.

# def pro1(v, lck):
#     lck.acquire()
#     while v.value < 10:
#         print(f"현재 증가 값은 {v.value}")
#         v.value +=1
#         time.sleep(1)
#     lck.release()



# def pro2(v, lck):
#     lck.acquire()
#     while v.value > -10:
#         print(f"현재의 값은 {v.value}")
#         v.value -=1
#     lck.release()

# if __name__ =='__main__':
#     # 데이터 공유를 위한 Value객체 생성
#     value = multiprocessing.Value('i', 0)
#     lock = multiprocessing.Lock() # 프로세스의 접근제어를 위한 Lock객체 생성
#     p1 = multiprocessing.Process(target= pro1, args=(value, lock))
#     p2 = multiprocessing.Process(target= pro2, args=(value, lock))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


# 현재 증가 값은 0
# 현재 증가 값은 1
# 현재 증가 값은 2
# 현재 증가 값은 3
# 현재 증가 값은 4
# 현재 증가 값은 5
# 현재 증가 값은 6
# 현재 증가 값은 7
# 현재 증가 값은 8
# 현재 증가 값은 9
# 현재의 값은 10
# 현재의 값은 9
# 현재의 값은 8
# 현재의 값은 7
# 현재의 값은 6
# 현재의 값은 5
# 현재의 값은 4
# 현재의 값은 3
# 현재의 값은 2
# 현재의 값은 1
# 현재의 값은 0
# 현재의 값은 -1
# 현재의 값은 -2
# 현재의 값은 -3
# 현재의 값은 -4
# 현재의 값은 -5
# 현재의 값은 -6
# 현재의 값은 -7
# 현재의 값은 -8
# 현재의 값은 -9




# --------------------------------------- 예제 : lock 을 지우고 해보자 -----------------
# import multiprocessing
# import time

# #  lock을 acquire 하면 해당 쓰레드만 공유 데이터에 접근할 수 있고, 
# # lock을 release 해야만 다른 쓰레드에서 공유 데이터에 접근할 수 있습니다.

# def pro1(v):
#     # lck.acquire()
#     while v.value < 10:
#         print(f"현재 증가 값은 {v.value}")
#         v.value +=1
#         time.sleep(1)
#     # lck.release()



# def pro2(v):
#     # lck.acquire()
#     while v.value > -10:
#         print(f"현재의 값은 {v.value}")
#         v.value -=1
#     # lck.release()

# if __name__ =='__main__':
#     # 데이터 공유를 위한 Value객체 생성
#     value = multiprocessing.Value('i', 0)
#     # lock = multiprocessing.Lock() # 프로세스의 접근제어를 위한 Lock객체 생성
#     p1 = multiprocessing.Process(target= pro1, args=(value, ))
#     p2 = multiprocessing.Process(target= pro2, args=(value, ))

#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()





# # 현재의 값은 0
# # 현재 증가 값은 0현재의 값은 -1

# # 현재의 값은 -2
# # 현재의 값은 -2
# # 현재의 값은 -3
# # 현재의 값은 -4
# # 현재의 값은 -5
# # 현재의 값은 -6
# # 현재의 값은 -7
# # 현재의 값은 -8
# # 현재의 값은 -9
# # 현재 증가 값은 -10
# # 현재 증가 값은 -9
# # 현재 증가 값은 -8
# # 현재 증가 값은 -7
# # 현재 증가 값은 -6
# # 현재 증가 값은 -5
# # 현재 증가 값은 -4
# # 현재 증가 값은 -3
# # 현재 증가 값은 -2
# # 현재 증가 값은 -1
# # 현재 증가 값은 0
# # 현재 증가 값은 1
# # 현재 증가 값은 2
# # 현재 증가 값은 3
# # 현재 증가 값은 4
# # 현재 증가 값은 5
# # 현재 증가 값은 6
# # 현재 증가 값은 7
# # 현재 증가 값은 8
# # 현재 증가 값은 9





# ------------------------ 예제 : lock 넣은 첫번째 예제의 코드 변수를 알아보기 좋게 수정 -----------------

import multiprocessing
import time

#  lock을 acquire 하면 해당 쓰레드만 공유 데이터에 접근할 수 있고, 
# lock을 release 해야만 다른 쓰레드에서 공유 데이터에 접근할 수 있습니다.

def pro1(v, lck):
    lck.acquire()
    while v.value < 10:
        print(f"현재 증가 값은 {v.value}")
        v.value +=1
        time.sleep(1)
    lck.release()

def pro2(v, lck):
    lck.acquire()
    while v.value > -10:
        print(f"현재의 값은 {v.value}")
        v.value -=1
    lck.release()

if __name__ =='__main__':
    # 데이터 공유를 위한 Value객체 생성
    value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock() # 프로세스의 접근제어를 위한 Lock객체 생성
    p1 = multiprocessing.Process(target= pro1, args=(value, lock))
    p2 = multiprocessing.Process(target= pro2, args=(value, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()