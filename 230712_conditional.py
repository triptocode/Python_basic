###################### if / elif (파이썬은 else if가 아님에 주의) / else  ####################
# if 조건: # 조건이 참인경우 아래의 실행코드 실행 
#      실행코드 #들여쓰기주의. 같은 계층의 인덴트는 모두 if문의 범주에 속함 




if(True): 
    print(1) # if문 조건이 True일때 : 이하가 실행됨

print(1) # indent 들여쓰기가 없으면 if문과 무관하게 출력됨

# if(True):
# print(1) # IndentationError

# 잘못된 성적출력 코드  / if 문으로만 여러조건을 설정하면 성능면에서도 안좋은편
# score=83 # B, C 가 출력됨
# if (score > 90):
#     print('A')
# if (score > 80):
#     print('B')
# if (score > 70):
#     print('C')


score=83 # 결과출력: B
if (100> score >= 90):
    print('A')
if 90> score and score >= 80:   ## () 소괄호 생략가능
    print('B')
if (80> score and score >= 70):
    print('C')


X=50
Y=10
if(X>Y):
    print('X is greater than B')
elif(X==Y):
    print('X is equal to Y')
else:
    print('Y is greater than X')


