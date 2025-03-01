#date: 01st March 2025
#Auhtor: Amrit Manash

#Strings slicing
my_chai = "Masala chai"
first_character = my_chai[0]
print(first_character)

print(my_chai[0:6]) #to extract the first word from string
print(my_chai[:]) #to print all the string
print(my_chai[2:]) #to print from index2 till last string
print(my_chai[:7]) #to print from index0 till index 6

#replace() method in string
print(my_chai.replace("Masala","Ginger"))

#split() method to convert string into list
my_chai = "masala,ginger,mint,lemon"
print(my_chai.split(","))

#find() method to search for character or word in string
#then it returns the starting index of that character or string
my_chai="Masala ginger chai"
print(my_chai.find("ginger"))

#count() method to find out the count of particular word or character
#in a string
my_chai="masala chai,ginger chai,lemon chai,mint chai"
print(my_chai.count("chai"))

#to convert a list into string using .join() method
my_chai = ["Lemon chai","Mint chai","Masala Chai"]
print(", ".join(my_chai))

#len() to find the length of string
my_chai = "masala chai"
print(len(my_chai))


