import random
letters=["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols=['!','<','>','@','%','*','^']

print("Welcome to the PyPassword Generator!")
no_letters=int(input("Enter no of letters you like to use in your password \n"))
no_symbols=int(input("Enter no of symbols you want to use in your password \n"))
no_number=int(input("Enter no of numbers you want to use in your password \n"))


# # easy steps
# password=""
# for char in range(1,no_letters+1):
#   password+=random.choice(letters)

# for char in range(1,no_symbols+1):
#   password+=random.choice(symbols)

# for char in range(1,no_number+1):
#   password+=random.choice(numbers)

# print(password)

# hard steps

password_list=[]
for char in range(1,no_letters+1):
  password_list+=random.choice(letters)

for char in range(1,no_symbols+1):
  password_list+=random.choice(symbols)

for char in range(1,no_number+1):
  password_list+=random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
  password+=char
print(f"your password is {password}")  