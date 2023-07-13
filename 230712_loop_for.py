# for문에 반복가능한 객체들: str, tuple, list, set , dict, range()

# for i in range(1,10,2):  # range(1이상, 10미만, 2씩 step 간격으로 )
#     #print(i, end=',') # 1,3,5,7,9,  // 출력 끝에 연결해서 찍음(옆으로 출력)
#     print(i, end=' ')  # 1 3 5 7 9  // 가로로 한줄 나옴 

# for i in range(1,10):
#     print(i) # 1~9 숫자가  세로로 숫자 하나씩 나열됨

# for i in range(1, 11):
#     print(2*i-1, end=' ') # 1 3 5 7 9 11 13 15 17 19 

# for i in {1,2,3}:
#     print(i)

# a= 'apple'
# for i in a:
#     print(i, end=' ') # a p p l e 

for i in {'이름': '홍길동', '주소':'파주시','전번':'01055558888'}:
    print(i) # key 만 출력됨 
# 이름
# 주소
# 전번

d = {'이름': '홍길동', '주소':'파주시','전번':'01055558888'}
print(d['이름']) # 홍길동
print(d['주소']) # 파주시






