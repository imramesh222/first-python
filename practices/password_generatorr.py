import random
letters = []

for ascii_value in range(ord('A'), ord('Z')+1):
    letters.append(chr(ascii_value))

for ascii_value in range(ord('a'), ord('z')+1):
    letters.append(chr(ascii_value))

print(letters)

symbols=['!','<','>','@','%','*','^']
print(symbols)


for numbers in range(10):
    print(numbers, end=' ')


print("Welcome to password generator! ")
no_numbers=int(input("Enter how many numbers do you want to add to your password"))
no_letters=int(input("Enter how many letters to add to your password"))
no_symbols=int(input("Enter how many symbols to add to your password"))

password_list=[]

for char in range(0,len(no_numbers+1)):
      password_list+=random.choice(numbers)

for char in range(0,len(no_letters+1)):
     password_list+=random.choice(letters)

for char in range(0,len(no_symbols+1)):
     password_list+=random.choice(symbols)

print(password_list)