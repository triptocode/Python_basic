# print((3==3) and (5!=3)) # True

# print(3=>3) # SyntaxError

# if 4<3:
#     print("when conditional is True, this sentence is printed!!!") 
                         #  아무결과도 출력안됨 [Done] exited with code=0 in 0.078 seconds
                         #  (조건이 True 일때만 실행하는데, 참이 아니라서)

# if 4<3:
#     print("when conditional is True, this sentence is printed!!!") 
# else:
#     print("when conditional is False, this sentence is printed!!!")


# if True:
#     print(1)
#     print(2)
# else:
#     print(3)
# print(4)



if True:
    if False:
        print(1)
        print(2)
    else:
        print(3)
else: 
    print(4)
print(5)  # 3과 5가 한줄에 하나씩 출력 



# greeting = input("hi입력:" )
# print(greeting*2)



#127 

resident_full_num= input("주민번호: ")
second_num = resident_full_num.split('-')[1]

if second_num[0]=="1" or second_num[0]=="3":     ##  주의 :"1" or "3" 으로 넣기! --> input()에넣은 숫자는 Str으로 인식 
    print("male")
elif second_num[0]=="2" or second_num[0]=="4":
    print("female")
else: print("false numbers! Try to type precise resident numbers!! ")



 ##  주의 :"1" or "3" 으로 넣기! ----> 이렇게 안하면 하단과 같이 else로 빠져서 동작됨. 
# if second_num[0]==1 or second_num[0]==3:
#     print("male")
# elif second_num[0]==2 or second_num[0]==4:
#     print("female")                                                   # input: 901010-235211  
# else: print("false numbers! Try to type precise resident numbers!! ") #false numbers! Try to type precise resident numbers!! 



#############  (1) Python String slicing   #############

# string[start:end:step]
# string[index (start) : index (end-1)]