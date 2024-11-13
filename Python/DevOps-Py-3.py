# #                   IF's & Then's                #
# #Ex 1
# def can_udrive ():
#     age=int(input("Enter your age (i cant breath) "))
#     if(age>=18):
#         print("You is gever yozem")
#     elif(age==16 or age==17 ):
#         print("Nah BRA")
#     else:
#         print("GET OUT")

# can_udrive()

# #Ex 2
# def odd_or_even (num):
#     return bool(num % 2 ==0)
# num=int(input("Pick a number dumass"))
# print(odd_or_even(num))

# #Ex 3
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

# #Ex 4
# def pos_nig (num=int(input("Enter A number"))):
#     if(num>=0):
#         return print(num>=0)
# pos_nig()

# #Ex 5
# def stalker ():
#     age=int(input("Enter u age "))
#     stu=str(input('is u student, yes/no only nig ')).lower()
#     while(stu!='yes' and stu!='no'):
#         stu=str(input('Those who know, Enter yes or no ')).lower()
#     if(age<18 or stu=='yes'):
#         return "you is yes discount"
#     return "you is not discount"

# print(stalker())

# #                    For and While Loops              #
# #Ex 6
# for x in range(1,11):
#     if x%2==0:
#         print(' ',x, end=' ' )

# #Ex 7
# sum_v1=0
# for y in range (101):
#     sum_v1+=y
# print('\n',sum_v1)

# sum_v2=sum(range(1,101))
# print(sum_v2)

# #Ex 8

# # print('x',end='')
# # for i in range(1,6):
# #     print(i,'|',end='')
# # print()
# # for j in range(1,6):
# #     print(j,' |',end='')
# #     for k in range(j,j*6,j):
# #         print(k,'|',end='')
# #     print()



## def multi_table(num:int):
##     print('x','  ',end='')
##     for i in range(1,num+1):
##         print(i,' ',end='')
##     print()
##     print('-------------------------------')
##     for j in range(1,11):
##         if(j<=9):
##             print(j,' |',end='')
##         else:
##             print(j,'|',end='')
##         for k in range(j,j*num+1,j):
##             if(k<=9):
##                 print(k,' ',end='')
##             else:
##                 print(k,'',end='')
##         print()


# multi_help=int(input("Enter Number for Multi Table"))
# multi_table(multi_help)


def multi_table(num:int):
    print('x','  ',end='')
    for i in range(1,num+1):
        if(i==num):
            print((f'\033[31m{i}\033[0m'),' ',end='')
        else:
            print(i,' ',end='')
    print()
    print('-'*num*4)
    for j in range(1,11):
        if(j<=9):
            print(j,' |',end='')
        else:
            print(j,'|',end='')
        for k in range(j,j*num+1,j):
            if(k<=9 and j*num==k):
                print((f'\033[31m{k}\033[0m'),' ',end='')
            elif(k<=9):
                print(k,' ',end='')
            elif(k==j*num):
                print((f'\033[31m{k}\033[0m'),'',end='')
            else:
                print(k,'',end='')
        print()
    


multi_help=int(input("Enter Number for Multi Table"))
multi_table(multi_help)

# def fac(n):
#     if n<0:
#         return('no')
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return n*fac(n-1)
# print(fac(5))


