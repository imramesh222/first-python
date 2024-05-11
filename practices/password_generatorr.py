letters = []

for ascii_value in range(ord('A'), ord('Z')+1):
    letters.append(chr(ascii_value))

for ascii_value in range(ord('a'), ord('z')+1):
    letters.append(chr(ascii_value))

print(letters)

symbols=['!','<','>','@','%','*','^']
print(symbols)


for i in range(10):
    print(i, end=' ')

print("Welcome to password generator! ")
no_numbers=input(int("Enter how many numbers do you want to add to your password"))
no_letters=input("Enter how many letters to add to your password")
no_symbols=input("Enter how many symbols to add to your password")

