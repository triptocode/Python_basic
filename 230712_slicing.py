
# 차량 번호 뒷자리 4개만 출력하기 
license_plate = "48가 0184"
print(license_plate[-4:])


lst = [1,2,3,4,5]
print(lst[:5]) # [1, 2, 3, 4, 5] // (앞 생략 =) index0 부터 : index 5 미만까지, 즉 index 4까지! 
print(lst[1:]) # [2, 3, 4, 5] // index 1 부터 : (생략) 마지막인덱스 value 포함한다!! (미만이 아님에)주의!!
print(lst[:3:]) # [1, 2, 3] // index 0 부터 : 3미만, 즉 index 2까지 : step은 생략하면 1
print(lst[::2]) # [1, 3, 5]


str1 = "홀짝홀짝홀짝"
print(str1[::2]) # 홀홀홀

str2 = 'PYTHON'
print(str2[::-1]) # NOHTYP

phone_num = "010-2222-3333"
extract_num = phone_num.replace("-"," ")
print(extract_num) # 010 2222 3333

url= "http://abc.kr"
url_split = url.split('.')
print(url_split)      # ['http://abc', 'kr']
print(url_split[-1])
