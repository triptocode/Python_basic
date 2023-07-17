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




# 210 아래 코드의 실행 결과는?
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


# B
# C
# B
# C
# B
# C
# A