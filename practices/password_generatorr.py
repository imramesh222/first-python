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
