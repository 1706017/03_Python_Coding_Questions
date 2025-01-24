"""
In Python we have 3 types of logical operator and , or , not
for and both the condition should be true than whole expression will be true
for or if any of the condition is true then whole expression will be true
for not it is just negation of current boolean if it is false and we apply not before that then it will be true
"""

has_good_income = True
has_good_credit = False
no_criminal_record = False

if has_good_income and has_good_credit:
    print("You are eligible for loan!! ")
elif has_good_income or no_criminal_record:
    print("You are eligible for loan!!")
else:
    print("Sorry you are not eligible for loan")

print("Thank you for using the application !!")

