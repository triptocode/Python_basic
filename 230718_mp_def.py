# # ############################################################################################
# # # module을 import하는 여러가지 방법

# # #import 모듈명
# # import multiprocessing
# # print(multiprocessing.cpu_count()) # 8     ★★★wn+R 에서 키워드 msinfo32를 검색★★★

# # # import 모듈명 as 모듈명의 별칭 
# # import multiprocessing as mp
# # print(mp.cpu_count())

# # # # from 모듈명 import* : 모듈속에 모든 클래스, 메서드, 변수등을 가져옴 
# # from multiprocessing import * 
# # print(cpu_count())


# #import 모듈명 import 함수명
# from multiprocessing import cpu_count
# print(cpu_count()) # 8

# # 함수를 별칭처리함 
# from multiprocessing import cpu_count as cc
# print(cc())

# #from 모듈명 import 변수명 
# from multiprocessing import current_process
# print(current_process().name) # MainProcess

# #from 모듈명 import 변수명 as 별칭
# from multiprocessing import current_process as cp
# print(cp().name)

# # 함수( 메서드)와 변수 import
# from multiprocessing import cpu_count, current_process
# print(cpu_count()) # 8 
# print(current_process().name) # MainProcess

# #함수와 변수 import시 별칭처리
# from multiprocessing import cpu_count as cc, current_process as cp
# print(cc()) # 8
# print(cp().name) # MainProcess

# ############################################################################################################


from multiprocessing import Process, freeze_support

#함수 정의
def Hello():
        print("Hello Process2")


#메인코드 부분: 함수 호출...
if __name__ == '__main__':  #스크립트의 진입점. # 파이썬은(객체지향언어이면서) 스크립트언어이다! 
                            #현재 스크립트가 직접 실행되는 경우만 코드블럭을 실행하도록 보장하는 용도
                            #다른 스크립트(.py) 임포트하면 실행x 
    freeze_support() #윈도우에서 multiprocessing을 사용할때 필요한 함수를 호출함
                     #멀티프로세싱처리할때 cpu, gpu 관계 
    p1 = Process(target=Hello) #Hello메서드를 실행할 프로세스 객체 생성 
    p1.start() # start()메서드가 호출되면 run()메서드가 자동 수행
    p1.join() # wait untill the process stops (사용이유: 다른 프로세스가 침범하지 못하게 해주려고! )
    p1.terminate()
    
