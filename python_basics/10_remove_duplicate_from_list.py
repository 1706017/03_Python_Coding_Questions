#Date : 26th Feb 2025
#Author : Amrit Manash

#Program to remove duplicate from list
my_list = [1,3,4,4,5,4,7,9,7]
unique_list = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)
