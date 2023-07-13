############################ 군집자료형 5가지 : str / list / tuple / set / dict  ############################

############################ 군집자료형 list  ############################

# li =list()
# print(li, type(li)) # [] <class 'list'>

# li =[1,2,3,4,5,6,7,8,9]
# print(li[0]) #1
# print(len(li)) # 9 - 데이터 갯수 

# print(li[0])
# print(li[1])
# print(li[8])  #리스트명[index넘버] : 인덱스위치에 있는 value값 자체 하나 출력// 인덱스는 0부터시작하니 인덱스8은 9번째 자리에 value값 9를 의미 : 
# print(li[len(li)-1]) # 9  // [len(li)-1] 는 li변수 데이터갯수인 9개-1 , 즉8이다. 
#                      # 그럼 li[8] 이고, index는8번째인 value값을 출력하는데 인덱스는0부터 시작이니 인덱스8은 9번째자리에 value값9가 나옴


# -----------------------------------------------------------------------------------------------
# li =[1,2,3,4,5,6,7,8,9]
# li[0] = 99     # [99, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li) 

# li[1] =[1,2,3] # [99, [1, 2, 3], 3, 4, 5, 6, 7, 8, 9]
# print(li) 

# li[2]='문자'   # [99, [1, 2, 3], '문자', 4, 5, 6, 7, 8, 9]
# print(li) 

# sli = "I'm studying list"
# print(sli[0:17:5]) # Itns   // index 0~ 17미만, 즉 인덱스 0~16까지, index0 데이터1개, 그후 5번째 간격으로 하나씩 출력
# print(sli[1:3])  # 'm   // index 1~ 3미만 = 즉, index 1,2 위치 value값들 2개:  'm 가 출력됨 

#################################  dictionary - 군집자료형 ##############################
#  dict 형태- {키1:값1, 키2:값2...}  // 딕셔너리는 json이랑 비슷해서 활용가능
# a = {'key': 'value', 1:[1,2,3], (1,2):'korea'}
# # print(a[1]) #a[1]에서 1은 키값이고, 키값을통해 value값 [1,2,3] 을 불러와 출력됨
# print(a['key']) # value
# print(a[(1,2)]) # korea
# print(type(a)) # <class 'dict'>

# d = {10:999, 
#      'a':[1,2,3],
#      (1,2): "aaa"
#     }
# print(d[10])
# print(d['a'])
# print(d[1,2]) 

########################### tuple - 군집자료형 ###########################
# tuple () : 중복o, list처럼 중복되나, list 는 [] / tuple은 () 소괄호 활용 
# score = (80, 90, 100,100) # (80, 90, 100, 100)
# print(score)

#################################  set - 군집자료형 ####################################
# set { }: 중복x , 인덱스 지원 x
# 즉 중복제거해줌 ex) list 형태 변수 a에 중복된 데이터가 있다면 set(a) 를 하면 a에 중복된 value값들은 하나만 담아 표현해줌

# 실습 - 아래 리스트[]에 데이터 중복을 제거해보자. / 힌트 set() 활용  
# a = [1,3,4,5,6,7,8,8,9,3,2,2,5,3]
# a.sort() # [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9]
# print(a)
# print(type(a)) # <class 'list'>

# a =set(a)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(a) 
# a = list(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)

# s1 = set([1,2,3,4,5])
# s2 = set([4,5,6,7,8])

# print(s1&s2) # {4, 5} // 교집합: & 
# print(s1|s2)        # {1, 2, 3, 4, 5, 6, 7, 8} // 중복제거 합집합
# print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8} // 중복제거 합집합  
# print(s1-s2)             # 차집합 {1, 2, 3}
# print(s1.difference(s2)) # 차집합 {1, 2, 3}

# s = {'가','나','다'}
# s.add('라')     # {'라', '다', '가', '나'} // 순서 믹스되서 나옴.
# print(s) 
# s.remove('라')  # {'가', '다', '나'} // 순서 믹스되서 나옴.
# print(s) 

# #s.update(5) #는 오류
# s.update([5])
# print(s)  # {5, '나', '가', '다'}


############# python - 40 page < handle values By converting tuple into a list > 
# reminder : Tuples are unchangeable !! so use a list !!
# T = (1,2,3,4,5,6,7,8)

# updateList = list(T) # Q1)  value 1 --> value 0
# updateList[0] = 0
# T = tuple(updateList)
# print(T) # (0, 2, 3, 4, 5, 6, 7, 8)

# addList = list(T) # Q2) add value 9
# addList.append(9) # append(value) : list 에서 맨뒤에 값 추가됨
# T = tuple(addList)
# print(T) # (0, 2, 3, 4, 5, 6, 7, 8, 9)

# deleteList = list(T) # Q1) remove value 8 
# deleteList.remove(8)
# T = tuple(deleteList)
# print(T) # (0, 2, 3, 4, 5, 6, 7, 9)



# print(bool([1,2,3])) # True
# print(bool(([])))    # False
# print(bool((1,2,3))) # True
# print(bool(1))       # True
# print(bool(0))       # False
# print(bool(()))      # False
# print(1 == 1) # True
# print(1 == 2) # False
# print(1>0)    # True
# print(2<1)    # False
# print(1>=1)   # True

# print(1!=0) #True //  T~와 같지 않다.

# a =True
# b = True
# print(a and b)   # True  // a =1 , b=1 1*1=1(True)
# a = False # a=0
# print(a and b)
# print(not a)
# print(not b)





