
# # 객체(=인스턴스) : 생산된 자동차 ,구워낸 붕어빵
# # 클래스 사용이유? 코드의 재사용을 제고.
# # 대형프로젝트 운영시 작성, 프로그램의 모듈화
# # # class 자동차: 
# # #     자동차 속성
# # #     색상
# # #     속도
# # #     기능
# # #     속도올리기()
# # #     속도내리기()


####################################### 클래스  ############################################

# class Car: # class start
#         # car field = var in class
#         color= "" #field1
#         speed = 0 #field2

#         def upSpeed(self, value): # method1. self: class.
#                 # self는 클래스의 변수(color, speed)를 참조하기 위하여 사용하는
#                 self.speed +=value #self.speed =self.speed+value
#                 #매개변수 value로 전달받은 값을 기존의 speed에 추가해라.
#         def downspeed(self, value): # method2
#                 self.speed -= value

# myCar1 = Car()
# myCar1.color ="red" # after creating instance, 
# myCar1.speed = 0    # created field (=var )of instance is made

# myCar2 = Car()
# myCar2.color = "blue"
# myCar2.speed = 0

# myCar3 = Car() # to create instance
# myCar3.color = "green" 
# myCar3.speed = 0

# myCar1.upSpeed(30)
# print("car color is %s, speed is %d 입니다" %(myCar1.color, myCar1.speed))

# myCar2.upSpeed(60)
# print("car color is %s, speed is %d 입니다" %(myCar2.color, myCar2.speed))

# myCar3.upSpeed(0)
# print("car color is %s, speed is %d 입니다" %(myCar3.color, myCar3.speed))


# ########### 매개변수가 없는 생성자 : 기본생성자 (메서드) ########################
# # 클래스 선언부 

# class Car:
#         color = ""
#         speed = 0


# def _init_(self):
#         self.color ='red'
#         self.speed =0

# def upSpeed(self, value):
#         self.speed += value

# def downSpeed(self, value):
#         self.speed += value
# myCar1 = Car()
# myCar2 = Car()

# print("Car1's color is %s, speed is %d" %(myCar1.color, myCar1.speed)) # Car1's color is , speed is 0
# print("Car2's color is %s, speed is %d" %(myCar2.color, myCar1.speed)) # Car2's color is , speed is 0





############################################ 매개변수가 있는 생성자 : 기본생성자 (메서드) ###################################
class Car:
        color = "" # instance var1. 각각의  인스턴스가 생성될때 그 인스턴스게 세팅됨 
        speed = 0  # instance var2. (인스턴스 변수)

        def __init__(self, value1, value2): # 주의:   Python에서  __ (underBar 두개쓰면 예약어니까 함수명으로 사용x  )
            self.color =value1
            self.speed =value2
        
        def upSpeed(self,value):
               self.speed +=value

        def downSpeed(self,value):
               self.speed -=value

    ##  main code 
myCar1 =Car("red", 30) #  myCar1변수로 인스턴스 생성과 동시에 두개의 argument를 넘겨줌 
myCar2 =Car("blue", 60)


print("Car1's color is %s, speed is %d" %(myCar1.color, myCar1.speed)) # 
print("Car2's color is %s, speed is %d" %(myCar2.color, myCar1.speed)) # 



##################################################  class var  클래스 변수 #############################################
# 여러개의 인스턴스들이 하나의 변수를 공유. 클래스 내의 전역 변수 

# class Car: 
#        color = "" # instance var1 (메서드안(객체안)에서 지역변수)
#        speed =0   # instance var2
#        count =0   # class var . (클래스전체에서 전역변수 같은 존재 )

#        def __init__(self):  # 기본생성자( 매개변수가 없는 생성자)
#               self.speed = 0  # self. 뒤에 작성해서 부르면 instance var! (인스턴스 변수)
#               Car.count +=1 # Car. (즉, 클래스명.)  뒤에 작성해서 부르면 class var(클래스 변수)


# # 변수 선언 부분
# myCar1, myCar2 = None, None # 변수선언부는 파이썬에서 생략가능하다. 

# # main code 부분
# myCar1 = Car() # 기본생성자로, argument가 필요 없다.   (myCar1 이 생성되면 관련된 메모리에 접근. myCar1에만 소속되어서 움직이는 지역변수 self.speed  ///// 반대로 Car.count 글로벌 변수로 Car1 / Car2 모두에 다 사용가능)
# myCar1.speed = 30

# print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총%d대 입니다" %( myCar1.speed, Car.count))  # 자동차1의 현재 속도는 30km, 생산된 자동차는 총1대 입니다

# myCar2 = Car() # 기본생성자로, argument가 필요 없다. 
# myCar2.speed = 60
# print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총%d대 입니다" %( myCar2.speed, Car.count))  # 자동차1의 현재 속도는 30km, 생산된 자동차는 총1대 입니다

# class Car:
#        pass # empty class declaration!  빈클래스선언 --> 문법오류방지


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# class Car: 
       
#        speed =0   
#        def upSpeed(self,value):
#                self.speed +=value
#                print(" current speed(슈퍼클래스): %d" % self.speed)

# class Sedan(Car): #슈퍼클래스 Car를 상속받음
#        def upSpeed(self,value):
#                self.speed +=value

#                if self.super > 150:               ####     AttributeError:'Sedan' object has no attribute 'super'        ######
#                       self.speed =150
#                       print("current speed (서브클래스): %d" % self.speed)
                
# class Truck(Car): 
#        pass  #슈퍼클래스의 모든 내용을 그대로 상속받음. 재정의 없음

# #변수선언 부분
# sedan1 , truck1= None, None

# # main code 부분 : 인스턴스 생성, 메서드 호출등..
# sedan1 = Sedan() # Sedan() 설게도로 부터 sedan1(인스턴스를 생성)
# truck1 = Truck()

# print("승용차--->", end="")
# sedan1.upSpeed(200)

# print("트럭--->", end="")
# truck1.upSpeed(200)

############################################### 특별한 메서드들 ####################################################
# class Line:
#        length = 0 
#        def __init__(self, length): #매개변수가 있는 생성자
#               self.length = length #매개변수 length값을 self.length에 저장하는 단계
#               print(self.length, "길이의 선이 생성되었습니다")
     
#        def __del__(self):
#             print(self.length, "길이가 삭제되었습니다.")
#        def __repr__(self):
#             return "선의길이: "+str(self.length)
#        def __add__(self, other):
#             return self.length + other.length
#        def __lt__(self, other):
#             return self.length < other.length
#        def __eq__(self, other):
#             return self.length == other.length
       

# # # main code 부분 : 
# myLine1 = Line(100)        
# myLine2 = Line(200) 

# print(myLine1) #__repr__() 메서드가 호출됨
# print("두선의 길이 합:" , myLine1+myLine2) # __add__() 호출

# if myLine1 < myLine2: #__lt__()
#       print(" myLine1선분의 길이가 myLine2보다 작다")
# elif myLine1 ==myLine2:
#        print("두 선분의 길이가 같다")
# else :
#       print(" myLine1선분의 길이가 myLine2보다 크다")


      
############################################### 추상 메서드들 ####################################################
# 빈껍질 메서드

######## 클래스 선언부분
class SuperClass:
      def method(self):
            pass #추상메서드
class subClass1(SuperClass):
      def method(self):
            print('SubClass1에서 method()를 오버라이딩 함')
class subClass2(SuperClass):
      pass # 향후 심각한 오류발생ㄱ ㅏ능성 있음 --> 오버라이딩 필요
          
## 메인코드 부분 ## 
sub1 = subClass1() # 인스턴스생성
sub2 = subClass2()

sub1.method() # subClass1에서 method()를 오버라이딩 함 
sub2.method() # 오버라이딩이 안되어서, 아무것도 출력x