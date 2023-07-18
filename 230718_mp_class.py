# from multiprocessing import Process, freeze_support

# class HelloProcess(Process): #Process클래스 상속
#     def __init__(self): #생성자메서드
#         super(Process, self).__init__() #슈퍼클래스의 Process클래스의 생성자 호출
#     def run(self):
#         print("Hello Process2")
# #main code 
# if __name__=='__main__':#
#     freeze_support() #윈도우 멀티프로세싱에서 필요
#     p1 =HelloProcess()
#     p1.start()
#     p1.join()
#     p1.terminate() # 생략해도 가능하나 좀비프로세스로 돌아다닐수 있어서 써줌. 생략하고 체크시 괜찮기는 했음


##################################################################################################################
from multiprocessing import Process, freeze_support

class HelloProcess(Process): #Process클래스 상속
    def __init__(self,arg1,arg2): #생성자메서드
        super(Process, self).__init__() #슈퍼클래스의 Process클래스의 생성자 호출
    def run(self): # run()메소드: 자동수행
        print("Hello Process2")
#main code 
if __name__=='__main__':#
    freeze_support() #윈도우 멀티프로세싱에서 필요
    p1 =HelloProcess(1,arg2='Hello') # 프로세스의 객체생성 p1
    p1.start() # start() 메소드가 호출되면 run() 메소드가 자동수행 
    p1.join()
    p1.terminate() # 생략해도 가능하나 좀비프로세스로 돌아다닐수 있어서 써줌. 생략하고 체크시 괜찮기는 했음

