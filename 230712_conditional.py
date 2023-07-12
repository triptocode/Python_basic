########## if ############
if(True): 
    print(1) # if문 조건이 True일때 : 이하가 실행됨

print(1) # indent 들여쓰기가 없으면 if문과 무관하게 출력됨

# if(True):
# print(1) # IndentationError

# 잘못된 성적출력 코드
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
