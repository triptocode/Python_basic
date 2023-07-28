## 데이터 공유 Value 클래스

import multiprocessing
import time

def pro1(v, pn):
    print(v)   # <Syncronized wrapper for c_long(0)
    print(v.value) # Value객체에 value 속성을 지정해서 데이터 값만 출력 
    print(f"{pn} Value 객체의 최 값: {v.value}") # 0
    # Value 객체에 value 속성을 지정해서 데이터 값만 출력
    time.sleep(1)


def pro2(v, pn):
    v.value= 10
    print(f"{pn} pro2에서 입력된 값: {v.value}")

## main code
if __name__ == "__main__":
    value = multiprocessing.Value('i', 0)
    # value = multiprocessing.Value('i')  --> 이렇게 적는걸축약한형태
    #데이터 공유를 위해 Value 객체생성 // i: 정수를의미, 0은 초기값
    p1 = multiprocessing.Process(target=pro1, args=(value, "p1"))# target= 함수명 , args= 그 함수의 매개변수
    p2 = multiprocessing.Process(target=pro2, args=(value, "p2"))# target= 함수명 , args= 그 함수의 매개변수

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    ## Value (args, 초기 값) 에 전달 할 수 있는 인자: arg는 str타입
    # b, B, u, h, i, I, l, L, q, Q, f, d
    # < -- array 모듈에서 가져온 값.
    # ex) Value ('i', 0)

    # =======================   참고.. 필기 못함 
