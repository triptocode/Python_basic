################################    프로세스를 시작 하는 방법 2가지   ###########################

# ------------------------------------ 스폰(Spawn)방식, 포크(fork) 방식 ----------------------------------

# 1. 스폰(Spawn)방식: 코드로 프로세스 생성           ex) window, linux, macOS
# 2. 포크(fork) 방식 - 부모 프로세스를 복제해서 생성.  ex) linux, macOS 
#                   - 프로세스 생성이 빠름
#                   - 그러나, 복제시 메모리상의 코드와 수많은 데이터가 한꺼번에 복제되서 시스템에 부하를 준다


# ---------------------------------------------    예제코드   ------------------------------------------
import multiprocessing

def start_process():
    return 1

# main code part
if __name__ == "__main__":
    p1 = multiprocessing.Process(target= start_process)
    p1.start()

    print(multiprocessing.get_start_method()) #spawn
    # 현재 파이썬이 돌고 있는 운영체제는 window이므로 기본 값
    # spawn방식으로 프로세스가 생성된다는 것을 알수  있다. 

    # 리눅스인 경우: 기본이 포크방식이고, spawn 방식으로 설정하기위해서는 
    # 아래와 같이 설정할 수 있다. 
    #multiprocessing.set_start_method("spawn")


################################    프로세스를 생성 하는 방법 3번째   ###########################
# fork server :  많은 서버가 있을 경우 중앙에 물어봐서 프로세스를 생성하는 방법
#  ex) linux , macOS

## 코드
# multiprocessing.set_start_method('forkserver')



#################################
# import _multiprocessing