# 사용자 정의 모듈 연습 : ex_module.py 와 ex_main.py 파일 두개 활용

# print("this code is excuted at the global level.")

# def some_func():
#  print("This is a function in the module ! ")



## 두번째 방법

def some_func():
 print("This is a function in the module ! ")


if __name__=="__main__":
 print("this code is excuted at the global level.")