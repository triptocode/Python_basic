###########################################    Module    ############################################

# # 1) 표준모듈
# # 2) 사용자모듈
# # 3) 외부모듈

# import turtle ## python 표준모듈(내장) turtle graphic

# t = turtle.Turtle() #turtle.Turtle(): 거불이 인스턴스생성(객체).인스턴스
# t.shape('turtle') #거북이 모양 생성
# t.forward(100) #전진 100
# turtle.exitonclick() #프로그램 종료를 위해서 클릭시 캔버스 닫힘. 

# # 주의: 파일명은 모듈명과 같지 않게 !!!

################################  turtle 모듈 : square 그리기 #########################################
# import turtle 
# t = turtle.Turtle()
# t.shape('turtle')
# for i in range(4):
#     t.forward(100)
#     t.right(90)          #it rotates in-place 90degrees clockwise
# turtle.exitonclick()



################################  turtle 모듈 : 분홍 별 그리기 #########################################

import turtle 
t = turtle.Turtle()
t.speed(10)
t.shape('turtle')
t.color('pink')
t.begin_fill()
for i in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()
turtle.exitonclick()


#######################################################################################################
# import turtle
# print(dir(turtle)) # turtle 모듈이 제공하는 함수목록 
# 출력:  ['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator', 'Turtle', 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__forwardmethods', '__func_body', '__loader__', '__methodDict', '__methods', '__name__', '__package__', '__spec__', '__stringBody', '_alias_list', '_make_global_funcs', '_screen_docrevise', '_tg_classes', '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities', '_turtle_docrevise', '_ver', 'addshape', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left', 'listen', 'lt', 'mainloop', 'math', 'mode', 'numinput', 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'warnings', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor']

# import sys
# print(sys.builtin_module_names)
# 출력: ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')

# import math
# print(dir(math))
# # 출력: ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


############################# calendar 
# import calendar
# print(calendar.calendar(2002))



####################################  time  ####################################
# import time

# # print(time.ctime())
# # print(time.time())
# # print(1)
# # time.sleep(5) # wait for 5min.
# # print(2)

# #------------------------------------
# for i in range(1,10):
#     print(i)
#     time.sleep(1)




########################################################################################3
########### 시간내 단어 입력하는 프로그램 ##################




########################################   random   ########################################

# import random

# words = ['a', 'b', 'c', 'd']
# print(random.choice(words)) 
# print(random.choice(words)) 
# print(random.choice(words)) 
# print(random.choice(words)) 

# # d
# # a
# # c
# # b


# a = range(1,10) # 1~ 9 까지 랜덤한 수 출력 
# print(random.choice(a))
# print(random.choice(a))
# print(random.choice(a))
# print(random.choice(a))

# # 5
# # 3
# # 8
# # 3

# colors = ['red', 'blue', 'green']
# print(colors[0])

# print(random.random())      # 0~1 사이 숫자가 랜덤하게 출력 (ex 0.520812219719507 )

# words2 = ['cookie', 'pear', 'walnut']
# print(int(random.random()*3))          # int 로  소수점 없에고 정수화
# print(words2[int(random.random()*3)])



# words2 = ['cookie', 'pear', 'walnut','blueberr','melon']
# print(words2[int(random.random()*5)]) # index 0~ 4 까지 (5*0.9= 4.5 인데 정수부분만 생각해서 4)