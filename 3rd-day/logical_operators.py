print("Welcome to Rollercoaster ride!\n")
height = int(input("Enter your height\n"))
bill = 0

if height >= 120:
    print("You are allowed to ride\n Now enter your age\n")
    age = int(input("Enter your age\n"))
    
    if age < 12:
        bill = 50
        print("Please pay Rs 50")
    elif age <= 18:
        bill = 70
        print("Please pay Rs 70")
    elif age>45 and age<55:
        bill==0
    else:
        bill = 100
        print("Please pay Rs 100")
    
        
    photo = input("If you would like to take photo, please enter Y otherwise N \n")  
    if photo == "Y" or photo == "y":  # Compare lowercase "y" as well
        bill += 30
        
    print(f"Your final bill is Rs {bill} only")
    
else:
    print("You are not allowed to ride")
