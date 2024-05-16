print("Tip Calculator")

bill=input("Bill amouunt")
print(type(bill))
no_of_person=input("No person person")
tip_percentage=input("Tip percentage you wolud like to give")
print(type(tip_percentage))
print(type(no_of_person))
total_tip=float(tip_percentage)*float(bill)/100
tip_per_person=float(total_tip)/int(no_of_person)
print(tip_per_person)

# print("Welcome to the Tip calculator")
# bill=input("What was the total bill amount?\n")
# percent=input("What percent tip of the total bill amount will you like to give?\n")
# no_of_person=input("How many people to spilt the bill?\n")

# tip=float(bill)*float(percent)/100
# per_person_tip=float(tip)/int(no_of_person)
# print(per_person_tip)

print("Welcome to the Tip calculator")
bill=input("What was the total bill amount?\n")
percent=input("What percent tip of the total bill amount will you like to give?\n")
no_of_person=input("How many people to spilt the bill?\n")

tip=float(bill)*float(percent)/100
per_person_tip=float(tip)/int(no_of_person)
print(per_person_tip)