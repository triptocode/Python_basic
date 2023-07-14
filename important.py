##############################################  127   ##############################################

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