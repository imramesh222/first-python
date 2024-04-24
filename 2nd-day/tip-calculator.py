print("Welcome to the Tip calculator")
bill=input("What was the total bill amount?\n")
percent=input("What percent tip of the total bill amount will you like to give?\n")
no_of_person=input("How many people to spilt the bill?\n")

tip=float(bill)*float(percent)/100
per_person_tip=int(tip)/int(no_of_person)
print(per_person_tip)