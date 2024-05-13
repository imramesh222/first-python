import random

rock="✊"
paper="📃"
scissors="✂"

userChoice=input("Enter your choice 0 for rock ,1 for sissors and 2 for paper:\n")

if userChoice==0:
  userChoice=rock
  print(f"You chose {userChoice}")
elif userChoice==1:
  userChoice=paper
  print(f"You chose {userChoice}")

elif userChoice==2:
  userChoice=scissors
  print(f"You chose {userChoice}")
else:
  print("Invalid choice")
  exit()

computerChoice=random.choice()