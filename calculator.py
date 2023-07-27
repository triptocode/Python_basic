


######################     1-1 에러 : UnboundLocalError: cannot access local variable 'result' where it is not associated with a value
# result = 0

# def add(num):
#     result += num
#     return result

# print(add(3))
# print(add(4))


######################     1-2 해결: 

# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(5))

######################    2-1 bad : None - 리턴값 없을때! calcalator 2개 

# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self,num):
#         self.result += num
#     def minus(self,num):
#         self.result -= num

# c1 = Calculator()
# c2 = Calculator()


# print(c1.add(3))
# print(c1.add(1))
# print(c2.add(5))
# print(c2.add(1))

# print(c1.minus(3))
# print(c1.minus(1))
# print(c2.minus(5))
# print(c2.minus(1))

# # None
# # None
# # None
# # None
# # None
# # None
# # None
# # None


######################    2-1 리턴값 없을때! calcalator 2개

# class Calculator:
#     def __init__(self):
#         self.result = 10

#     def add(self,num):
#         self.result += num
#         return self.result
#     def minus(self,num):
#         self.result -= num
#         return self.result
# c1 = Calculator()
# c2 = Calculator()


# print(c1.add(1))
# print(c2.add(5))

# print(c1.minus(5))
# print(c2.minus(5))

# 11
# 15

# 6
# 10


######################    2-1 리턴값 없을때! calcalator 

# class Calculator:
#     def __init__(self):
#         self.result = 10

#     def add(self,num):
#         self.result += num
#         return self.result
#     def minus(self,num):
#         self.result -= num
#         return self.result
# c1 = Calculator()
# c2 = Calculator()


# print(c1.add(1))
# print(c1.minus(5))



######################    3-1 calcalator - 키보드로 입력받은 사칙연산 타입별  두수 계산기 

class Calculator():
    
    # 초깃값 설정
    def __init__(self, num1, num2, cal_type):
        self.num1 = num1
        self.num2 = num2
        self.cal_type = cal_type
    # 사칙연산 공식    
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    
    # 계산방식에 따라 계산하는 함수 생성
    def startCalculate(self):
        print("\n계산 결과는 아래와 같습니다.\n")
        
        # 계산방식 = "더하기"
        if self.cal_type == "add":
            print(self.add())
        # 계산방식 = "빼기"
        elif self.cal_type == "minus":
            print(self.sub())      
        # 계산방식 = "곱하기"
        elif self.cal_type == "multiply":
            print(self.mul())     
        # 계산방식 = "나누기"
        else:
            print(self.div())
        

# 계산할 두 수 입력받기
num1 = int(input("수를 입력하세요.:"))
num2 = int(input("수를 입력하세요.:"))

# 계산방식 입력받기
cal_type = input("계산 사칙연산 키워드중 하나를 선택 입력하세요. [옵션: add, minus, multiply, divide] :")

# 계산기 클래스에 인자 넣기
MyCalculator1 = Calculator(num1, num2, cal_type)

# 계산 결과 출력
MyCalculator1.startCalculate()