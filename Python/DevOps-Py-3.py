#                   IF's & Then's                #
#Ex 1
# def can_udrive ():
#     age=int(input("Enter your age (i cant breath) "))
#     if(age>=18):
#         print("You is gever yozem")
#     elif(age==16 or age==17 ):
#         print("Nah BRA")
#     else:
#         print("GET OUT")

# can_udrive()

#Ex 2
# def odd_or_even (num):
#     return bool(num % 2 ==0)
# num=int(input("Pick a number dumass"))
# print(odd_or_even(num))

#Ex 3
# def grade_u(grade):
#     if (type(grade) is not int and type(grade) is not float):
#         return ('Error Enter A Number')
#     if(grade == 100 or grade >= 90):
#         return str('A')
#     elif(grade == 89 or grade >= 80):
#         return str('B')
#     elif(grade == 79 or grade >= 70):
#         return str('C')
#     elif(grade == 69 or grade >= 60):
#         return str('D')
#     return str('F')
# print(grade_u(78))

#Ex 4
# def pos_nig (num=int(input("Enter A number"))):
#     if(num>=0):
#         return print(num>=0)
# pos_nig()

#Ex 5
# def stalker ():
#     age=int(input("Enter u age "))
#     stu=str(input('is u student, yes/no only nig ')).lower()
#     while(stu!='yes' and stu!='no'):
#         stu=str(input('Those who know, Enter yes or no ')).lower()
#     if(age<18 or stu=='yes'):
#         return "you is yes discount"
#     return "you is not discount"

# print(stalker())

#                    For and While Loops              #
#Ex 6
# for x in range(1,11):
#     if x%2==0:
#         print(' ',x, end=' ' )

#Ex 7
# sum_v1=0
# for y in range (101):
#     sum_v1+=y
# print('\n',sum_v1)

# sum_v2=sum(range(1,101))
# print(sum_v2)

#Ex 8
##Version 1.0
# print('x',end='')
# for i in range(1,6):
#     print(i,'|',end='')
# print()
# for j in range(1,6):
#     print(j,' |',end='')
#     for k in range(j,j*6,j):
#         print(k,'|',end='')
#     print()


#Version 2.0
# def multi_table(num:int):
#     print('x','  ',end='')
#     for i in range(1,num+1):
#         print(i,' ',end='')
#     print()
#     print('-------------------------------')
#     for j in range(1,11):
#         if(j<=9):
#             print(j,' |',end='')
#         else:
#             print(j,'|',end='')
#         for k in range(j,j*num+1,j):
#             if(k<=9):
#                 print(k,' ',end='')
#             else:
#                 print(k,'',end='')
#         print()


# multi_help=int(input("Enter Number for Multi Table"))
# multi_table(multi_help)


# Function Print & Highlight Multipications of {num}
# def multi_table(num:int):
#     print('x','  ',end='')
#     for i in range(1,num+1):
#         if(i==num):
#             print((f'\033[31m{i}\033[0m'),' ',end='')
#         else:
#             print(i,' ',end='')
#     print()
#     print('-'*num*4)
#     for j in range(1,11):
#         if(j<=9):
#             print(j,' |',end='')
#         else:
#             print(j,'|',end='')
#         for k in range(j,j*num+1,j):
#             if(k<=9 and j*num==k):
#                 print((f'\033[31m{k}\033[0m'),' ',end='')
#             elif(k<=9):
#                 print(k,' ',end='')
#             elif(k==j*num):
#                 print((f'\033[31m{k}\033[0m'),'',end='')
#             else:
#                 print(k,'',end='')
#         print()
    

# multi_help=int(input("Enter Number for Multi Table"))
# multi_table(multi_help)


#Function For finding square {num}, print & highlight in multi table

# def multi_table(num:int):
#     print('x','  ',end='')
#     for i in range(1,11):
#         if(i==num):
#             print(i,' ',end='')
#         else:
#             print(i,' ',end='')
#     print()
#     print('-'*num*4)
#     for j in range(1,11):
#         if(j<=9):
#             print(j,' |',end='')
#         else:
#             print(j,'|',end='')
#         for k in range(j,10*j+1,j):
#             if(k<=9 and num**2==k):
#                 print((f'\033[31m{k}\033[0m'),' ',end='')
#                 square_num=k
#             elif(k<=9):
#                 print(k,' ',end='')
#             elif(k==num**2):
#                 print((f'\033[31m{k}\033[0m'),'',end='')
#                 square_num=k
#             else:
#                 print(k,'',end='')
#         print()
#     return square_num

# multi_help=int(input("Enter Number for Multi Table"))
# x=multi_table(multi_help)
# print(x)


#Ex 9
# col_lst=['red','green','blue','yellow']
# for color in col_lst:
#     print('welcome color',color)

#Ex 10
# count=10
# while count>=1:
#     print('bip '*count)
#     count-=1

#Ex 11
# import random
# rng=random.randint(1,10)
# guess=int(input("Guess A number between 1-10 included: "))
# while (not (1<= guess <=10)):
#     guess=int(input("Only numbers between 1-10 ma nigga: "))
# while guess!=rng:
#     last_guess=guess
#     if guess > rng:
#         guess=int(input('Try Lower '))
#     if guess < rng:
#         guess=int(input('Try Higher '))
#     else:
#         print(f'nice nigga the number is {guess} ')
# print('yay the number was ',rng) 

#Ex 12
# out=0
# sum=0
# while out >=0:
#     out=int(input("Enter Numbers, To end type a nigative Number"))
#     sum+=out

# print("Ma boi the sum is ",sum)

#Ex 13
# def greet():
#     print('Yo Yo Mada Phlaka')
# greet()

#Ex 14
# def greet_name(name=str(input("Enter Ya Name : "))):
#     print(f'Welcome to O Block {name}')

# greet_name()

#Ex 15 Weve Done it with out project multi table

#Ex 16
# def fac(n):
#     if n<0:
#         return('no')
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return n*fac(n-1)
# print(fac(5))

#Ex 17
# def find_max(lst:list):
#     max=lst[0]
#     for num in range(1,len(lst)):
#         if(lst[num]>max):
#             max=lst[num]
#     return max
# lst=[1,5,3,200,9,2,100]
# max_num=find_max(lst)
# print(max_num)

#Ex 18
# def c_t_f(temp=int(input("Enter Temperature"))):
#     print(f'{temp}° Celsius is {9/5*temp+32}° Fahrenheit')
# c_t_f()

#Ex 19
# def is_paly(word=str(input("Enter a word "))):
#     if word in word[::-1]:
#         print(f'{word} is a palindrome')
#     else:
#         print(f'{word} is not a palindrome')
# is_paly()

#Ex 20
# def sum_ls(ls:list):
#     sum=0
#     for num in ls:
#         sum+=num
#     return sum
# print(sum_ls([10,20,5,2,8]))

#Ex 21
# def check_prime(num=int(input("Enter a Num : "))):
#     if num < 1:
#         return print('GET OUT')
#     if num == 2:
#         return print('Yes Primer')
#     for x in range(2,int(num**0.5)+1):
#         if num%x==0:
#             return print('GET OUT')
    
#     return print('From the screen 💻 to the ring 💍 to the PEN 🖊️to the king 🤴')
# check_prime()


#Ex 22
# def cal(num1:int,num2:int,operation:str):
#     if operation not in['+','-','*','/']:
#         return print("Invalid Operator")
#     if(num1==0 or num2==0 and operation=='/'):
#         return print('cant use / on 0')
#     return print(eval(f'{num1} {operation} {num2}'))
        
# cal(2,2,'/')