###################################  클래스 Overriding #############################################

# class C1:
#     def __init__(self):  #  __init__(self)는 메서드 생성자
#         print("생성자 입니다.")

# test = C1()

###################################  클래스 Overloadding #############################################
# # use methods with the same name

# --------------class definition 
# class Calculator:

#     def add(self, a, b):
# 	    return a+b 
# 	def add(self, a, b, c):           ########### def에 빨간밑줄.. 파이썬에서는 오버로딩 지원x //   def add(self, a, b, c=0):  넣으면 TypeError! 안난다고? 하지만 def에 빨간줄~
# 	    return a+b+c


# # main code - instance craetion, method call 
# calc = Calculator() # instance craetion --> calc변수에 대입 --> 인스턴스명 
# result1 = calc.add(2,3)
# print("두수의합: ", result1)

# result2 = calc.add(2,3,4)
# print("두수의합: ", result2)


# ----------------------> 2개의 메소드가 동작한것은 아니다? 두번째 메소드만 동작? 위치바꾸면 첫번째가 동작할까? / 파이썬에서 오버로딩을 지원하지 않는다? 

# 메소드 오버로딩 (Method Overloading)
# 중복정의
# 메소드 오버로딩은 동일한 클래스 안에서 메소드 이름이 같지만 매개변수의 개수, 자료형이 다른 것을 의미한다.
# 파이썬은 메소드 오버로딩을 지원하지 않는다.
# 동적 타입 검사 -> 실행 시 타입 검사(타입 에러가 실행시에 발견)









