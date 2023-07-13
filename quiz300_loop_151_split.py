# Python String split

fileList = ['prj1.c','prj1.py','prj2.c','prj2.py', 'prj1.h']
for file in fileList:
 spl= file.split(".")
 if(spl[1]=="h") or(spl[1]=="c"):
     print(file)