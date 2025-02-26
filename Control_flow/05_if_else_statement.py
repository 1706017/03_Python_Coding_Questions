#Date: 26th Feb 2025
#Author : Amrit Manash

#if else statement

marks = float(input("Enter your marks"))

if marks > 40:
    print("you are pass")
else:
    print("Sorry you are fail")

#if elif and else statement

age = int(input("Enter your age"))
nationality = input("ENTER your nationality")
nationality_v1 = nationality.upper()
if age >=18:
    print("WELCOME TO VOTING MACHINE!!")
    if nationality_v1=="INDIAN":
        print("You are eligible for casting vote")
    elif nationality in ('bhutan','nepal'):
        print("You are eligible for casting vote but after 1 month")
    else:
        print("Sorry you are not eligible for voting")

else:
    print("Sorry you are not eligible for voting")

print("Thank you for using this voting application!!")

