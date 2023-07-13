# 주의: input()은 String으로 인식하는게 default! 
# 숫자계산 하려면 int()로 변환해줘야한다. 

# name = input("Enter your name: ")
# print(name)    

# num2 =input("Enter your phone number: ")
# num= int(num2)
# print(num)

# num2 =input("Enter number: ")
# print(num2)

####################################### input() 입력데이터는 string타입! num을 넣어도 string타입이됨
####################################### print()안에 문자변수+문자변수 가능!-->예: print("string" +num) 
# a =input("Enter number1: ") # 2
# b =input("Enter number2: ") # 3
# print("sum : "+a+b)   # 23  // input()은 String으로 인식하는게 default! 

####################################### input() string타입!으로인식되니 숫자화하고, 연산은 int()를 사용 
####################################### print()안에 문자변수+숫자변수 불가능!--> print("string" +num) 에러발생 TypeError

# 숫자계산 하려면 int()로 변환해줘야한다. 
strNum1 =input("Enter number3: ") # 2
intNum1=int(strNum1)
strNum2 =input("Enter number4: ") # 3
intNum2=int(strNum2)
print("sum: ",intNum1+intNum2)    # 5
# 주의 : print("sum: "+intNum1+intNum2)  -> 에러발생 TypeError: can only concatenate str (not "int") to str