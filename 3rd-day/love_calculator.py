print("Love Calculator!")
name1=input("Enter your name: ")
name2=input("Enter your partner name: ")
combined_string=name1+name2
lowercase_string=combined_string.lower()
t = (lowercase_string.count("t"))
r = (lowercase_string.count("r"))
u = (lowercase_string.count("u"))
e = (lowercase_string.count("e"))

true=t+r+u+e
print(true)

l = (lowercase_string.count("l"))
o = (lowercase_string.count("o"))
v = (lowercase_string.count("v"))
e = (lowercase_string.count("e"))

love=l+o+v+e

print(love)

love_score=str(true)+str(love)

int_love_score=int(love_score)


if (int_love_score<10) or (int_love_score>90):
  print(f"Your love score is {love_score}%, you go together like coke and mentos.")
elif (int_love_score>=40) and (int_love_score<=50):
  print(f"Your love score is {int_love_score}%, you are alright together.")
else:
    print(f"Your love score is {int_love_score}%")


