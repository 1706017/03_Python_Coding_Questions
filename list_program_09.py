"""
List in python is a built in data type that stores multiple value
and those value can be of different data types

"""
#Creation of list in python

skills = ["python","azure","sql","web_development"]
print(skills)
print(type(skills))

# To access the specific element from list using index

print(skills[1]) #azure
print(skills[0:2]) #python,azure

#To know the length of list
print(len(skills)) #4

#We can store different data types in a string unlike arrays
employee = ["Amrit",27,"Patna"]
print(employee) #Amrit,27,Patna

#Lists are mutable that means unlike strings we can change the value of lists
employee[2] = "Bhagalpur" #so here we are updating the value in a list
print(employee) #Amrit,27,Bhagalpur

#List Slicing it is similar to string slicing in python
marks = [78,90,36,89,98,23]
print(marks[0:]) #[78,90,36,89,98,23]
print(marks[1:4]) #[90,36,89]
print(marks[:]) #[78,90,36,89,98,23]
print(marks[:4])#[78,90,36,89]
print(marks[-1]) #[23]









