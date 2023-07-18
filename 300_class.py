class Human:
    pass

areum = Human() #  Human()--> 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩



# 254
class Human:
    def __init__(self):
        print(" Human class has become an instance! ")

person = Human()




# # 255
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")
# print(areum.name) # 아름
# print(areum) # <__main__.Human object at 0x0000023DB5E4B390>