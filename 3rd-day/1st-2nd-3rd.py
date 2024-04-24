# def main():
#   number=int(input("Enter a number: \n"))
#   if number %2 ==0:
#     print("even")
#   else:
#     print("odd")
# main()


# age=int(input("Enter age: \n"))
# premium=input("Enter premium (yes or no): \n")

# if age>=18:
#   print("allowed")
#   if premium=='yes':
#     print("Premium page")
#   else:
#     print("Normal page")
# else:
#   print("Not allowed")

height=int(input("Height in cm"))

if height>=120:
  print("You are allowed to ride")
  age=int(input("Age"))
  if age <12:
    print("Please pay Rs 50")
  elif age>=12 and age<18:
    print("Please pay Rs 70")
  else:
    print("Please pay Rs 100")
else:
  print("You are not allowed to ride")





