# # height=int(input("Enter your height\n"))
# # bill=0
# # if height>=120:
# #   print("You are allowed to ride")
# #   age=int(input("Enter your age\n"))
# #   if age <12:
# #     bill=50
# #     print("Please pay Rs 50")
# #   elif age <=18:
# #     bill=70
# #     print("Please pay Rs 70")
# #   else:
# #     bill=100
# #     print("Please pay Rs 100")
# #   photo=print(input("If you would like to take photo, please enter Y otherwise N \n"))
# #   if photo=="Y":
# #     bill=bill+30
# #   print(f"Your final bill is Rs {bill} only")
# # else:
# #   print("You are not allowed to ride")


# height = int(input("Enter your height\n"))
# bill = 0

# if height >= 120:
#     print("You are allowed to ride")
#     age = int(input("Enter your age\n"))
    
#     if age < 12:
#         bill = 50
#         print("Please pay Rs 50")
#     elif age <= 18:  # Changed to elif to avoid redundant checks
#         bill = 70
#         print("Please pay Rs 70")
#     else:
#         bill = 100
#         print("Please pay Rs 100")
        
#     photo = input("If you would like to take photo, please enter 'Y' otherwise 'N' \n")  # Removed print from here
#     if photo == "Y":
#         bill += 30  # Shortened bill incrementation
        
#     print(f"Your final bill is Rs {bill} only")
    
# else:
#     print("You are not allowed to ride")

print("Welcome to rollercoaster rode")

height = int(input("Enter your height\n"))
bill = 0

if height >= 120:
    print("You are allowed to ride")
    age = int(input("Enter your age\n"))
    
    if age < 12:
        bill = 50
        print("Please pay Rs 50")
    elif age <= 18:
        bill = 70
        print("Please pay Rs 70")
    else:
        bill = 100
        print("Please pay Rs 100")
        
    photo = input("If you would like to take photo, please enter Y otherwise N \n")  
    if photo == "Y" or photo == "y":  
        bill += 30
        
    print(f"Your final bill is Rs {bill} only")
    
else:
    print("You are not allowed to ride")

