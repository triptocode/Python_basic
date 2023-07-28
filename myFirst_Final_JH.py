# a = 1+2j
# print(type(a)) # <class 'complex'>

# num = 123
# print(type(num)) # <class 'int'>
# # print(len(num))  # TypeError: object of type 'int' has no len()

# str1 ="123"
# str2 ="가나다"
# str3 ="abc"
# print(len(str1)) # 3
# print(len(str2)) # 3
# print(len(str3)) # 3


# # string 은 인덱스 값을 가짐
# str ="가나다"
# print(str[0]) #가 
# print(str[1]) #나 
# print(str[2]) #다 
# # print(str[3]) # IndexError: string index out of range

# # =============================================#
# a = "hi"
# print(id(a)) # 2542658353072 ---> 객체 주소값 반환 
# str4 ="가나다라마"
# print(str4[-1]) #마  , 즉 뒤에서 첫번째
# print(str4[0:2]) #가나  , index0~ 1까지 [2미만]
# print(str4[:2]) #가나  , index0~ 1까지 [2미만]  , 첫인덱스 0 생략가능
# print(str4[1:2]) #나  , index1~ 1까지 [2미만]
# print(str4[:]) #가나다라마 , 처음부터 끝까지 
# print(str4) #가나다라마 , 처음부터 끝까지 



# a = "1,2,3,4,5,6,7,8,9" #""는 문자열
# print(len(a)) #쉼표도 문자열의 길이에 포함되므로 17이 나온다.
# print(a[::2]) # 123456789 , step은 2라 쉼표까지 카운트해서 2번째마다 출력
# b="대한민국"
# print(b[::-1]) #국민한대 , 역순출력
# print(b[::-2]) #국한

# ###############문자열의 함수#####################################

# # str.find("value")  ---->  index넘버를 찾아줌
# a ="가나다라마"
# help(a.find) # 문법 도움말 , find단어를 ctrl+클릭

# print(a.find("가")) # 0, 
# print(a.find("마")) # 4

# print(a.split("다")) #['가나', '라마']
# print(a.replace("나","★")) # 가★다라마
# print(a) # 가나다라마 , 위의 replace/ split 함수로 변한 값이 저장되진 않음

# # 새변수명을 같은변수명을 활용하여 담아서 저장하여 출력방법은 있다. - 하단참고
# a= a.replace("마","★") #가나다라★
# print(a)

# print(9/3) #3.0 
# print(type(9/3)) # <class 'float'> 

# print(8/3)  # 2.6666666666666665
# print(int(8/3)) # 2 (정수int로 타입변환)
# print(8//3) # 2  (소수점이하 버림)
# print(9%5)  # 4 (5로 나누고 (몫은1) 나머지 값 4출력)


# #divmod()함수 - 113






# #####매개변수가 있는 생성자메서드 #################
# class Car:
#     color = ""      # 인스턴스변수, 각각의
#     speed = 0       # 인스턴스변수

#     def __init__(self, value1, value2):  #두 개의 매개변수(파라미터)
#         self.color = value1
#         self.speed = value2

#     def upSpeed(self, value):
#         self.speed += value

#     def downSpeed(self, value):
#         self.speed -= value

#     ###메인코드 부분
# myCar1 = Car("빨강", 30)    #인스턴스 생성과 동시에 두개의 아규먼트를 생성자메서드에게 넘겨줌
# myCar2 = Car("파랑", 60)

# print("자동차1의 색상은 %s이며, 현재의 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
# print("자동차2의 색상은 %s이며, 현재의 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))






# ### 클래스 변수 #########################
# #: 여러 개의 인스턴스들이 하나의 변수를 공유. 클래스 내의 전역변수
# class Car:
#     color = ""  #인스턴스변수1, 메서드 만의 지역변수
#     speed =0    #인스턴스변수2
#     count = 0   #클래스 변수, 클래스 전체에서 전역변수 같은 존재

#     def __init__(self): #기본생성자 :매개변수가 없는 생성자
#         self.speed = 0  #)(인스턴스변수)self 올 부르면 인스턴스 변수이고
#         Car.count += 1  #(클래스변수)Car.으로 변수를 부르면 클래스변수인 것을 알 수 있다.

# #변수 선언 부분:
# myCar1, myCar2 = None, None  #변수 선언부는 생략가능.

# #메인코드 부분
# myCar1 = Car()  #기본 생성자이므로 아규먼트 필요없음.
# myCar1.speed = 30
# print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다." % (myCar1.speed, Car.count))

# myCar2 = Car()  #기본 생성자이므로 아규먼트 필요없음.
# myCar2.speed = 60
# print("자동차2의 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다." % (myCar2.speed, Car.count))


# class Car:
#     pass  #빈클래스 선언 ---> 문법 오류 방지




################ 메서드 오버라이딩 : 서브클래스에서 슈퍼클래스의 메서드를 재정의 #######

# class Car:
#     speed = 0
#     def upSpeed(self, value):
#         self.speed += value

#         print("현재 속도(슈퍼 클래스): %d" % self.speed)  # 포매팅 방식
#         # print("현재 속도(슈퍼 클래스): %d" ,self.speed)

# class Sedan(Car):   #슈퍼클래스 Car를 상속받음.
#     def upSpeed(self, value):
#         self.speed += value

#         if self.speed > 150:        #오버라이딩 된 부분
#             self.speed = 150
#             print("현재 속도(서브 클래스):%d" % self.speed)

# class Truck(Car):
#     pass        #슈퍼클래스의 모든 내용을 그대로 상속받음. 재정의 없음.

# # #변수 선언 부분 (생략가능)
# # sedan1, truck1 = None, None

# ##메인코드 부분 : 인스턴스 생성, 메서드 호출 등...
# sedan1 = Sedan()  #Sedan()설게도로부터 sedan1(인스턴스)를 생성
# truck1 = Truck()

# print("승용차 -->",end="[end]")
# sedan1.upSpeed(200)     #메서드 호출

# print("트럭-->",end=" ")   #
# truck1.upSpeed(200)






# ########## 특별한 메서드들 #################################
# class Line:
#     length = 0
#     def __init__(self,length): #매개변수가 있는 생성자
#         self.length = length  #매개변수 length값을 self.length에 저장
#         print(self.length, "길이의 선이 생성되었습니다.")

#     def __del__(self): #인스턴스가 삭제될 때 호출되는 메서드
#         print(self.length, "길이의 선이 삭제되었습니다.")

#     def __repr__(self): #print(메서드)
#         return "선의 길이:" + str(self.length)
#     def __add__(self,other): #덧셈
#         return self.length + other.length
    
#     def __lt__(self,other): # <
#         return self.length < other.length

#     def __eq__(self,other): # ==
#         return self.length == other.length

# ##메인 코드 부분
# myLine1 = Line(100) #첫번째 인스턴스가 생성됨과 동시에 생성자(__init__())를 부름.
# myLine2 = Line(200) #두번째 인스턴스 두 인스턴스의 length 비교

# print(myLine1) #print(인스턴스명)를 수행할 때 __repr__()메서드 호출됨

# print("두 선의 길이 합:", myLine1 + myLine2)    #__add__()호출

# if myLine1 < myLine2: #__lt__()
#     print('선분 2가 더 기네요')
# elif myLine1 == myLine2:    #__eq__()
#     print('두 선분의 길이가 같네요')
# else:
#     print('모르겠네요')

# del(myLine1)  # __del__()

# # # 100 길이의 선이 생성되었습니다.
# # # 200 길이의 선이 생성되었습니다.
# # # 선의 길이:100
# # # 두 선의 길이 합: 300
# # # 선분 2가 더 기네요
# # # 100 길이의 선이 삭제되었습니다.
# # # 200 길이의 선이 삭제되었습니다.






# # ########################### 추상 메서드 ###########################
# # #빈껍질 메서드

# # ###클래스 선언부분

# class SuperClass:
#     def method(self): # self 안넣어도 작동함. 무슨차이? 
#         print("슈퍼클래스")
# class subClass1(SuperClass):
#     def method(self):
#         print("subClass1안에서 함수=메서드를 overriding ! ")
# class subClass2(SuperClass): # SuperClass 안넣어도 작동함. 무슨차이? 
#     def method(self):
#        pass
       

# sub1 = subClass1
# sub2 = subClass2

# sub1.method() # subClass1안에서 함수=메서드를 overriding !
# sub2.method() # 반응 없음 

