
############## Python ver.3 부터는 import collections.abc 폴더안에 들어간걸로 변경됨에 주의 ################

import collections.abc

# obj = [1,2,3,4]
# obj2 = {1,2,3,4}
# obj3 = "abcdef"
# obj4 = {'a':1, 'b':'aa', 'c':3}
# obj5 = (1,2,3,4)
# obj6 = range(10)
# obj7 = range(1,10)

# print(isinstance(obj,collections.abc.Iterable))   #True // Iterable 하면 True or False 를 반환함 
# print(isinstance(obj7,collections.abc.Iterable))  #True
# # isinstance() 메소드를 통해 해당 객체가 반복가능한 객체인지 아닌지 확인가능 
# # isinstance() --> bool
# # range(10) range(0,10)

# ld = list(range(10)) 
# print(ld)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ld2 = ['a',9,[1,2,3],('a','b')]
# print(range(len(ld2)))    # range(0, 4)

# for i in ld2:
#     print(i)

# for i in (range(len(ld2))):   #ld2넣으면 range(4) // 숫자 0~ 3까지 하나씩 출력됨 
#     print(i)

# for i in (range(len(ld2))):
#     print(ld2[i])  #  모든 values 들이 하나씩 출력됨 

# for j in (1,2,3,4): 
#     print(j, end =',') # 1,2,3,4,

# for i in [1,2,3,4]: 
#     print(i, end ='-') # 1-2-3-4-


################################### loop 제어문 여러개 사용시, 들여쓰기 주의! #######################333

for i in [1,2,3]:      # list    1 일때       / 2 일때 
    for j in (1,2,3):   # tuple  1,2,3,4      / 1,2,3,4
      print(j, end =',')
    print(i, end ='번째끝') 
# 1,2,3,1번째끝1,2,3,2번째끝1,2,3,3번째끝

# for i in [1,2,3]:      # list    1 일때       / 2 일때 
#     for j in (1,2,3):   # tuple  1,2,3,4      / 1,2,3,4
#       print(j, end =',')
#       print(i, end ='번째끝')  
# 1,1번째끝2,1번째끝3,1번째끝1,2번째끝2,2번째끝3,2번째끝1,3번째끝2,3번째끝3,3번째끝

