#                     Tuples                     #
#Ex 1
my_tuple=(1,2,3)
print(my_tuple[1])
#my_tuple[1]=20 gives error

#Ex 2
person=('ILAN',21,'Kiryat Ono')
name,age,city=person[0],person[1],person[2]
print(name,age,city)

# Ex 3
nested_tuple=((1,2,3),(4,5,6))
print(nested_tuple[1][1])

#Ex 4
numbers=(1,2,3,2,4,2)
print(numbers.count(2))
print(numbers.index(3))

#                  Dictionaries               #
# Ex 1
student={'name' : 'George','age' : 21,'grade' : 'Nigger'}
print(student['name'])
student['school'] = 'Ben Zvi'
print(student)

#Ex 2
student.update({'age': 22})
print(student)

student.pop("grade")
print(student)

print('grade' in student)

#Ex 3
capitals={'France' : 'Paris','Spain' : 'Madrid','Japan' : 'Tokyo'}
for country,capital in capitals.items():
    print(f'Country is {country} Capital is {capital}')

#Ex 4
print(capitals.values())
print(capitals.keys())
print(capitals.items())

#Ex 5

# Version 1.0
text='hellllllllllllllllllo'
output={}
for chr in text:
    if chr not in output:
        output[chr]=text.count(chr)

print(output)

#Version 2.0
tex='hello'
outputty={}
for chr in text:
    if chr in outputty:
        outputty[chr]+=1
    else:
        outputty[chr]=1
print(outputty)

#                Sets                  #

#Ex 1
my_set={1,2,3,4,5}
my_set.add(6)
my_set.add(3)
my_set.remove(2)
print(my_set)

#Ex 2
set_A={1,2,3,4}
set_B={3,4,5,6}
set_C=set_A.union(set_B)
print(set_C)
set_C=set_A.intersection(set_B)
print(set_C)
set_C=set_A.difference(set_B)
print(set_C)
set_C=set_A.symmetric_difference(set_B)
print(set_C)

#Ex 3
numbers_lst=[1,2,2,3,4,4,5]
set_dup=set()
set_dup.update(numbers_lst)
print(set_dup)

#Ex 4
print(3 in set_A)
print(6 not in set_A)


