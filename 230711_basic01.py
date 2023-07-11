# a=1
# b='가'
# c="나"
# print(a)
# print(b)
# print(c)


# c=12345
# print(type(c))
# print(str(c))
# c=str(c) #c의 타입을 str형으로 변환
# print(type(c))
# a="안녕하세요 \n 제 이름은 김정환 입니다. \n 잘부탁드립니다."
# print(a) #\n은 엔터키에 해당 
# print(5+3)
# print(3-2)
# sum=5+3
# print(sum)
# sub=3-2
# print(sub)
# mul=4*3
# print(mul)
# print(type(9/3)) #float 3.0 나누기의 결과값은 무조건 실수형이다.
# print(5/3)
# print(type(5/3))
# c=int(5/3) #기존의 데이터타입을 정수타입으로 변환
# print(type(c))
# print(c)
# print(5//3) # 5/3을 한후 소수점이하를 버림 1이 출력됨 
# print(5%3)
# print(5**3) #5의 세제곱 
# a=5
# a+=3
# print(a)
# a-=2
# print(a)
# b=5
# b**=3
# print(b)
# #divmod 함수 
# divmod(5,3)
# print(divmod(5,3))
# #pow()함수 제곱할때 쓰임 
# print(pow(5,3))
#cos,sin,tan 등을 계산할때 제공되는 모듈이 있다:math 
# import math #math.py를 불러들임
# print(math.sqrt(8)) #제곱근을 계산함 2.8284271247461903
# 리스트 값 변경이 가능 []
#임의의 객체(아무값이나)를 순서대로 저장하는 집합형태의 자료형 

# a=[1,2,3,4]
# print(type(a))
# print(a)
# a=[1,2,[1.1,2],'a']
# print(a[2])
# print(a[0])
# print(a[0:4])
# a=[4,1,3,2]
# a.append(5) #끝에 5를 추가함
# print(a)
# a.remove(2) #리스트에서 2를 제거 
# print(a)
# a.sort() #정렬함수 오름차순으로 
# print(a)


# x =[1,2,[1.1,2],'a']
# print(x[2]) #[1.1,2]
# y = a[2]
# print(y)
# y.remove(2)
# print(y)
# x[2] =print(y)


######################### 230711 - 파이썬 2일차 #######################
# c= [4,1,3,2] # [4, 1, 3, 2]
# print(c) 
# c.append(5) # [4, 1, 3, 2, 5]
# print(c)
# c.sort() #[1,2,3,4,5]   순서정렬: 작은수 --> 큰수 
# print(c) 

# c.remove(1)
# print(c) # [2,3,4,5]  

# print(c.remove(2)) # None // 제거하는 함수니까 당연 리턴값이 없고.. 바로 출력안됨(remove, reverse 둘다).
# print(c) # [3,4,5] 

# print(c[-1])  # 5 // 역순으로 첫번째 인덱스
# print(c[-2])  # 4 // 역순으로 두번째 인덱스
# print(c[::-1]) # [5, 4, 3] //  ::는 전체 /// -1 은 역순  
# print(c)  # [3, 4, 5]      //  역순은 c에 저장되지 않고 나오는데.. 
# c.reverse() # reverse()를 넣으면 역순이 c에 저장되어 아래처럼 출력됨 
# print(c) # [5, 4, 3]

# b = 0b11
# print(type(b)) # <class 'int'>
# print(b) # 즉, 2진수 11은 3(00,01,10,11,100,101,110,111,1000)

# c=0o12
# print(type(c)) # <class 'int'>
# print(c) # 10

# d = 0x23 # 접두어 0x  는 16진수
# print(type(d)) # <class 'int'>
# print(d) # 35

# type_is ="123"
# print(type(type_is)) # <class 'str'>
# number = 12313131313123143546546563442342342425464565475
# print(type(number)) # <class 'int'>

# num =2e-4 # -4: 소수자리가 4자리 늘어남
# print(type(b))
# print(b) # 0.0002
# c = 3e3 #e3: 정수부에서 3자리를 이동
# print(type(c)) # <class 'float'>
# print(c) #3000.0

# ###############3 문자열 자료형 ###########
# f='1'
# print(type(f))  # <class 'str'>
# g="Hi"
# print(type(g)) # <class 'str'>

# print(1+2)     #3
# print('1'+'2') #12
# print(type('1'+'2')) # <class 'str'>
# str1 ='hello'
# str2 ='world'
# print(str1+str2) # helloworld

# print(2*3) #6
# print('2'*3) #222  // 반복연산자 
# print('문장맨뒤에공백넣고반복출력 '*3) #문장맨뒤에공백넣고반복출력 문장맨뒤에공백넣고반복출력 문장맨뒤에공백넣고반복출력 



# a ='12345'
# b = '34567'
# c =a[0:3] +b[1:] #a는 a[0]~a[2]까지, b[1:]-b[1] ~ 끝까지
# print(c) # 1234567

# spell='abcdefghi'
# print(spell.upper()) # ABCDEFGHI
# spell='ABCDEFGHI'
# print(spell.lower()) # abcdefghi
# spell='abCDefgHi'
# print(spell.swapcase()) # ABcdEFGhI

# a='abcde'
# print(a.replace('cd','3')) # ab3e

# a=['a','b','c']
# print(a) # a=['a','b','c']
# print('#'.join(a))  # 출력결과는 a#b#c

# a = 'abcd abcd'
# print(a.capitalize()) # Abcd abcd

# b = 'abcd abcd'
# print(b.title()) # Abcd Abcd

# b = '   abcd abcd   '
# print(b) #    abcd abcd    // 앞뒤 공백 같이 출력
# print(b.strip()) #abcd abcd// strip()은 앞뒤 공백제거
# print(b)  #    abcd abcd    // 다시 본래값 앞뒤 공백 같이 출력
# print(b.lstrip())  ## 출력값에 마우스 드래그 하여 공백길이 확인/비교 가능
# print(b.rstrip())  ## 출력값에 마우스 드래그 하여 공백길이 확인/비교 가능


