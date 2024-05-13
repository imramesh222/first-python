import random
letters=["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols=['!','<','>','@','%','*','^']

print("Welcome to password generator ")

no_letters=input(int("Enter no of letters you want ton use \n"))
no_numbers=input(int("Enter no of numbers you want to use \n"))
no_symbols=input(int("Enter no of symbols you want to use \n"))

password_list=[]
for char in no_letters:
  password_list+=random.choice(no_letters)

for char in no_numbers:
  password_list+=random.choice(no_numbers)

for char in no_symbols:
  password_list+=random.choice(no_symbols)

print(password_list)