########## 매개변수가 있는 생성자메서드 #########################
########## self 파헤치기 #####################################
# self는 클래스 객체 자신이다.
class Car : 
    color = ""      #인스턴스 변수. 각각의 인스턴스가 생성될때 그 인스턴스 소속 필드로 세팅됨
    speed = 0       #인스턴스 변수

    def __init__(self, value1, value2):  #2개의 매개변수(파라미터)
        self.cont = self
        print(f"self매개변수의 값 : {self.cont}, 데이터타입: {type(self)}")
        self.color = value1
        var_loc = id(self.color)
        print(f"color변수의 메모리위치 : {var_loc}")
        self.speed = value2
        print(f"speed변수의 메모리위치 : {id(self.speed)}")

    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed -= value
    
    ##메인코드 부분(인스턴스 생성)
myCar1 = Car("빨강", 30)    #인스턴스 생성과 동시에 두개의 아규먼트를 생성자메서드에게 넘겨줌
print(f"myCar1의 내용 : {myCar1}")
myCar2 = Car("파랑", 60)    #인스턴스가 생성되면 생성자 호출

print("자동차1의 색상은 %s이며, 현재의 속도는 %dkm 입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s이며, 현재의 속도는 %dkm 입니다." % (myCar2.color, myCar2.speed))