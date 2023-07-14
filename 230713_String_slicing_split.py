#############  (1) Python String slicing   #############

# string[start:end:step]

my_str = "This is a substring tutorial"
result1 = my_str[0:4]                  # 문자열 앞에서 원하는 갯수만큼 자를때 string[0:len]
print(result1) # This

result2 = my_str[:7]                  # 0은 생략가능 string[:len]                                      
print(result2) # This is


#############  (2) Python String split    #############

# string.split(separator, maxsplit) 
# separator: optional. default -1, which is "all occurences"
# split() method splits a string into a list
# default separtor is any whitespace

txt = "Welcome to Korea"
result = txt.split()
print(result) # ['Welcome', 'to', 'Korea']


txt2 = "studying String split, loop for, conditional if."
result2 = txt2.split(",")
print(result2) # ['studying String split', ' loop for', ' conditional if.']

# setting maxsplit parameter to n, will return a list with (n+1) elements
# below maxsplit 2 --> 2+1 = 3elements 
str = "a/b/c/d/e/f"
result3 = str.split("/",2)
print(result3) # ['a', 'b', 'c/d/e/f']