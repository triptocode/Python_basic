
##  ============================================= 예제1) 첫번째 : 실행run 하면 에러나는 multiprocessing 코드  ==============================
# import multiprocessing
# import time

# #함수 선언부분
# def worker_function(name, delay):
#     print(f"Worker {name} 시작")
#     time.sleep(delay)
#     print(f"Worker {name} 종료")

# #메인 코드부분

# process1 = multiprocessing.Process(target=worker_function, args=("프로세스", 2))  # wait for 2 seconds
# #Process() 클래스로부터 프로세스객체 생성->생성되면 (target=함수명) 함수가 호출됨) / args 인자name에 값은 "프로세스" 이며, 2초간 대기
# process2 = multiprocessing.Process(target=worker_function, args=("프로세스", 3))  # wait for 2 seconds

# # 실행
# process1.start()
# process2.start()

# #대기
# process1.join()
# process2.join()

##종료
#print("모든 프로세스 종료")

# # 실행시 에러발생 
# # RuntimeError:
# #         An attempt has been made to start a new process before the
# #         current process has finished its bootstrapping phase.

# #         This probably means that you are not using fork to start your
# #         child processes and you have forgotten to use the proper idiom
# #         in the main module:

# #             if __name__ == '__main__':
# #                 freeze_support()
# #                 ...

# #         The "freeze_support()" line can be omitted if the program
# #         is not going to be frozen to produce an executable.
# # 종료되었습니다



##  ========================================== 예제2) 두번째 : 실행run 하면 정상작동하는 multiprocessing 코드  ==============================
import multiprocessing
import time

#함수 선언부분
def worker_function(name, delay):
    print(f"Worker {name} 시작")
    time.sleep(delay)
    print(f"Worker {name} 종료")

#메인 코드부분   // # 주의 :  ""안에 공백 있으면 안됨! " __main__"  ==> 오류나 작동x
if __name__=='__main__': # 추가된 부분?  -  예제1)과 다르게 추가된 코드 

    process1 = multiprocessing.Process(target=worker_function, args=("프로세스", 2))  # wait for 2 seconds
    #Process() 클래스로부터 프로세스객체 생성->생성되면 (target=함수명) 함수가 호출됨) / args 인자name에 값은 "프로세스" 이며, 2초간 대기
    process2 = multiprocessing.Process(target=worker_function, args=("프로세스", 3))  # wait for 2 seconds

    # 실행
    process1.start()
    process2.start()

    #대기
    process1.join()
    process2.join()

    #종료
    print("모든 프로세스 종료")

# Worker 프로세스 시작
# Worker 프로세스 시작
# Worker 프로세스 종료
# Worker 프로세스 종료
# 모든 프로세스 종료