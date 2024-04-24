# print("Welcome to Pizza ordering system!")
# size=input("What size of pizza do you order? , 'S','M' OR 'L' \n")

# s_price=15
# m_price=20
# l_price=25
# if size=='S':
#   print(f"Your Pizza will be Rs {s_price}")
# if size=='M':
#   print(f"Your Pizza will be Rs {m_price}")
# else:
#   print(f"Your Pizza will be Rs {l_price}")
#   add_pepperoni=input("Do you want to add Pepperomi to your Pizza?'\n")
#   if add_pepperoni=='Y':
#     if size=='S':
#       s_price+=5
     
#       if size=='M' and size=='L':
#         m_price+=7
#         l_price+=7
        
#         extra_cheese=input("Do you want to add extra cheese to your Pizza?'\n")
#         if extra_cheese=='Y':
#           s_price+=2
#           m_price+=2
#           l_price+=2
#           print(f"Your Pizza will be Rs {s_price} 'or' {m_price} 'or' {l_price}")


print("Welcome to Pizza ordering system!")
size =input("What size you want to order? 'S','M' or 'L'\n")


bill=0
if size =="S" :
  bill+=15
elif size == "M":
  bill+=20
else :
  bill+=25

add_pepperoni=input("Do yoiu want to add pepporoni? 'Y' or 'N'\n")
if add_pepperoni=="Y":
  if size=="S":
    bill+=2
  else :
    bill+=3
extra_cheese=input("Do you wan tto add extra cheese? 'Y' or 'N'\n")
if extra_cheese=="Y":
  bill+=1
  print(f"Your final bill is Rs {bill}")


