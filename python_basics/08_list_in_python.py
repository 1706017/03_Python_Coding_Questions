#Date : 26th Feb 2025
#Author : Amrit Manash

#List
'''
List in python is a inbuilt data type
It has below features
a) Mutable -> its value we can change
b) Ordered -> it maintains the sequence in which value is added in list
c) Hetrogenous -> It can contain multiple value of same of differnt data type

'''
print("About myself:")
my_info = ['Amrit Manash',27,"Bihar",52000.0]
for i in my_info:
    print(i)


#Indexing in list : It means we can access the element in list via index
print("My name is :",my_info[0])
print("My age is :",my_info[1])

#List slicing :
print(my_info[0:2])
print(my_info[1:])
print(my_info[:])
print(my_info[-1])



