# print("★ 구구단을 출력합니다.\n")
# for x in range(2, 10):
#     print("------- [" + str(x) + "단] -------")
#     for y in range(1, 10):
#         print(x, "X", y, "=", x*y)
# print("---------------------")

# def gugu():
#     for i in range(1, 10):
#         print(f"{2}x{i}={2*i}") # formatting 방법: f"{}{}"
# gugu() #실행! --함수명() 형태로 호출하여야만 해당함수가 실행됨

# help(gugu) # Help on function gugu in module __main__:

########################## 함수의 매개변수 ############################
# def func(x): #x는 매개변수
# 주의: 함수를 호출할때 arguement의 갯수는 반드시 파라미터개수와 일치하여야 함 

# def func(a,b,c):
#     print(a,b,c)
# func(1,2)  # TypeErro  - 인자와 파라미터 갯수 일치해서 호출해야함 

# def gugu(x):                       # x 는 파라미터 또는 매개변수라고 함 // 매개변수는 함수속에 선언되어 있음
#     for i in range(1,10):
#         print(f"{x}x{i}={x*i}")
# gugu(3)                           # 3 은 인자값 = argument 
# gugu(4)
# gugu(5)



# def gugu(x=2):                    # 기본값 세팅한 경우   
#     for i in range(1,10):
#         print(f"{x}x{i}={x*i}")

# # gugu(5)
# gugu()  # 인자 안넣고 호출가능한경우는 오직, 기본값 세팅된경우만(여기서는 x=2) 출력됨


## 97page - global var , local var  - def

