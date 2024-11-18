#                    Basic File Operations with Date Logging                #


#Calculator
# def calc(num1:int,operation:str,num2:int):
#     print('-'*24)
#     for i in range(10):
#         if i==1:
#             print('|',num1,operation,num2,'=',(f'\033[31m{eval(f'{num1} {operation} {num2}')}\033[0m'))
#             print('|'+'-'*22+'|')
#         if i==3:
#             print('| ',7,'  ',8,'  ',9,'  ','x','   |')
#         if i==5:
#             print('| ',4,'  ',5,'  ',6,'  ','-','   |')
#         if i==7:
#             print('| ',1,'  ',2,'  ',3,'  ','+','   |')
#         if i==9:
#             print('| ',0,'   ','-','    ','=','     |')
#         print('|',' '*16,'    |')
#     print('-'*24)
# num1=int(input("Enter First Number : "))
# operation=str(input("Enter Operator : "))
# num2=int(input("Enter Second Number : "))
# calc(num1,operation,num2)

#Ex 1
import datetime
import os
date1=datetime.datetime.now()
date2=date1.strftime("%Y-%m-%d %H:%M:%S")
if os.path.exists("./DevOps-1144-git/Python/Exer1.txt")==False:
    file=open("./DevOps-1144-git/Python/Exer1.txt","x")
write=str(input('Enter Content : '))
while 'done' not in write:
    file=open("./DevOps-1144-git/Python/Exer1.txt","a")
    file.write(str(date2)+' '+write+"\n")
    file.close()
    write=str(input('Enter Content to Stop type "done" :  '))

file=open("./DevOps-1144-git/Python/Exer1.txt","r")
print(file.read())
file.close()

#Ex 2
# file=open("./DevOps-1144-git/Python/Exer1.txt","r")
# for line in file:
#     print(line)
# file.close()

#Ex 3
# more=str(input("Would you like to add more enteries ?? (yes/no)"))
# while 'no' not in more:
#     file=open("./DevOps-1144-git/Python/Exer1.txt","a")
#     write=str(input('Enter Content : '))
#     file.write("\n"+' '+write+str(date2))
#     more=str(input("Would you like to add more enteries ?? (yes/no)"))
# file.close()

#Ex 4
file=open("./DevOps-1144-git/Python/Exer1.txt","r")
count_lines=0
count_words=-1
for lines in file:
    count_lines+=1
    for words in lines[20:].split(" "):
        count_words+=1
print("Number Of Enteries : ",count_lines,"Number Of Words : ",count_words )
file.close()





