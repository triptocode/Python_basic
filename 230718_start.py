# 참고 f 포매팅
s = 'coffee'
n = 5
result1 = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result1)



# # [[ 참고2 ]])  ---- line33번의 튜플 args=(i,) 의미  : , 컴마를 찍어서 int=정수가 아니라 (여러 element)를 넣은 (튜플)로 인식하게 해준다. 
type((1))
print(type((1))) # <class 'int'>

type((1,))
print(type((1,))) # <class 'tuple'>

#############################################################################################################
# 함수로 4개의 프로세스를 생성하는 프로그램. 
import multiprocessing

def worker_process(name): 
    #각 프로세스의 작업을 정의합니다.
    print(f"Worker Process{name} started")
    #해당 프로세스가 시작됨을 출력

# 스크립트가 import된것이 아니라 직접 수행될때( = import된게 아니라 직접작성?)아래의 코드블럭에 수행을 보장하는 역할  
if __name__ =='__main__':
    
    num_processes = 4 #프로세스 수 # 생성할 프로세스의 수를 지정
    processes = []  #프로세스 리스트 # 빈리스트를 processes라는 변수에 할당 

    #멀티프로세스 생성 및 시작
    for i in range(num_processes): # range(4) 와 동일 - line.10 참고
        p = multiprocessing.Process(target= worker_process, args=(i,)) # target = 실행할 함수, 즉 worker_process(name) 함수실행.  args=(i,)는 name파라미터에 들어가는 인자값
        p.start()
        processes.append(p) #프로세스를 리스트에 추가함  # 주의: p.append(p) 로 작성하면 안됨 

    for p in processes:
        p.join() # 각 프로세스의 종료를 대기함 

    print("All processes completed") 

# [ 출력결과 : ]
# Worker Process0 started
# Worker Process2 started
# Worker Process3 started
# Worker Process1 started
# All processes completed

