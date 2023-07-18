def add(a,b):
    return a+b

def printSomething(a,b,c):
    print(a,b,c)

def printLogo():
    print('logo text ...')

c=add(1,2)               # 출력되는건 없다  
printSomething(1,2,3)    # 1 2 3
printLogo()              # logo text ...




def func(*args):
      print(args)
      print(type(args))


func(1, 2, 3, 4, 5, 6, 'a', 'b') 
    # (1, 2, 3, 4, 5, 6, 'a', 'b')
    # <class 'tuple'>




def sum_all(*numbers):
      result = 0
      for number in numbers:
           result += number
      return result

print(sum_all(1, 2)) #
print(sum_all(1, 2, 3, )) #