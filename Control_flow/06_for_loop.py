#Date: 26th Feb 2025
#Author : Amrit Manash

#looping through a list using for loop
my_skills = ['ADF','ADB','Python','SQL']
for i in my_skills:
    print(i)
print("Above are my skills")

#looping through string using for loop
my_name = "Amrit Manash"
for i in my_name:
    print(i)

#use of range() function
sum = 0
for i in range(0,11):
    sum = sum + i
    print(i)
print("The sum value from 0 to 10 is",sum)

#Nested for loop
x=[1,2,3]
y=[4,5,6]
for i in x:
    for j in y:
        print(i,j)
