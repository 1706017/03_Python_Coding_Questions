#using ' and " both in a single string in python
stmt = "Amrit is a good developer and Amrit's favorite Programming language is python"
print(stmt)


#Indexing of strings in python
name = "Amrit Manash"
print(name[0])  #A
print(name[-1]) #h
print(name[-2]) #s
print(name[0:3]) #Amr
print(name[0:]) #Amrit Manash
print(name[1:]) #mrit Manash
print(name[:6]) #Amrit
print(name[:]) #Amrit Manash
print(name[1:-1]) #mrit Manas


#Formatted Strings in python
name = "Amrit Manash"
fav_pro_lan = "Python"
print(f"My name is {name} and my favorite programming language is {fav_pro_lan}")


#Some basic string methods
name = "Amrit Manash"
print(name.upper())
print(name.lower())
print(name.find('M')) #it returns the index value
print(name.replace('Manash','King')) #replaces the old string with the new
print(len(name))
print("Manash" in name) #return Boolean True or false





