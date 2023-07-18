# # range(start, stop, step)
# # start : 0 이 default
# # stop :  N 개 length / 0 ~ (N-1) 숫자 출력
# # step:  

# def  print_coin():
#  print("비트코인")

# for i in range(3):
#  print_coin()

# # 비트코인
# # 비트코인
# # 비트코인

# for num in range(3):
#  print(num)
#  num
# # 0
# # 1
# # 2




# # 210 아래 코드의 실행 결과는?
# def message1():
#     print("A")

# def message2():
#     print("B")

# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()

# message3()


# # B
# # C
# # B
# # C
# # B
# # C
# # A




# ###################### 300제 211 #######################
# # 1) error
# # def 함수(a, b) :
# #     print(a + b)
# # 함수("안녕", 3)     ## str +int 는 TypeError: must be str, not int

# # 2) 정상작동
# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", str(3))  # str+str 이어야 더하기 함수 잘 작동

# # 215  문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력
# def print_with_smile (string) :
#     print (string + ":D")


# print_with_smile("hi ") # hi :D



#219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

print_arithmetic_operation(1,2)