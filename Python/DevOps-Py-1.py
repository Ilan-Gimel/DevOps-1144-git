#Ex 1
age=21
name='GeverYozem'
print(f'my name is : {name} and im {age} years old')

#Ex 2
x=10
y=5
sum=[x,y]
print(sum[0] + sum[1])
print(sum[0] - sum[1])
print(sum[0] / sum[1])
print(sum[0] * sum[1])

# Ex 3
a=3
b=7
a,b = b,a
print(a,b)

#Ex 4
length=float(input("Enter Length : "))
width=float(input("Enter Width : "))
area=length * width
print(f'the area of the rectangle is : {area}')

#Ex 5
greeting='Hello World!'
print(len(greeting))
print(greeting[0])
print(greeting[-1])

#Ex 6
first_name=str(input("Enter First Name"))
last_name=str(input("Enter Last Name"))
full_name=first_name + ' ' + last_name
print(full_name)

#Ex 8
quote='Youre either erect or your not me'
print('Nigga ' + quote.upper())
print(quote.lower())

#Ex 9
word='Molester'
print(word[0:3])
print(word[-3:])
print(word[::-1])

#Ex 10
sentence='Pdf File is the Sigma Balls'
print(sentence.replace('Sigma Balls','GeverYozem'))

#Ex 11
text='Nigger Bigger Shigger Trigger Finger Jiggler Singer'
print('Trigger' in text)
print('George Floyd' in text)

#Ex 12
list1=['Mango','mango','MANGO','MaNgO']
list1.append('MAngO')
list1.pop(0)
print(list1)

#Ex 13
animals=['Blacks','Mexican','Hindu','Indians','Balkans']
print(animals[0])
print(animals[-1])
print(len(animals))

#Ex 14
numbers=[69,420,666,911,1337]
numbers[1]=12
print(numbers)
numbers.append(30)
print(numbers)
numbers.pop()
print(numbers)

#Ex 15
numi = list(range(1,11))
print(numi)
print(numi[0:5])
print(numi[-3:])
numi.reverse()
print(numi)

#Ex 16
list_num=[1,2,3,4,5]
list_sqrt=[]
for i in list_num:
    list_sqrt.append(i**2)
print(list_sqrt)

#Ex 17
list_item=['mango','mango','mango','banana','mango','banana']
print(list_item.count('mango'))
print(list_item.count('banana'))

#Ex 19
numbers_1=[1,2,3]
numbers_2=[4,5,6]
numbers_1+=numbers_2
print(numbers_1)
numbers_1.append(4)
print(numbers_1)

#Ex 20
#Version 1.0
def remove(lst,value):
    for i in range(len(lst)-1,-1,-1):
        if (lst[i]==value):
            lst.pop(i)
#Version 2.0
def remove2(lst,num):
    while num in lst:
        lst.remove(num)
#Version 3.0        
def remove3(lst, num):
    lst[:] = list(filter(lambda x: x != num, lst))
#Version 4.0
def remove4(lst,num):
    lst[:]=[x for x in lst if x != num]

remove(numbers_1,4)
print(numbers_1)

print(list(range(7,0,-1)))


#Ex 21
#Bubble Sort
ass_num=[4,9,23,5,3,9,12]
for i in range(len(ass_num)):
    for j in range(len(ass_num) -i -1):
        if(ass_num[j]>ass_num[j+1]):
            ass_num[j],ass_num[j+1]=ass_num[j+1],ass_num[j]
print(ass_num)
