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

computerChoice=random.randint(0,2)

if computerChoice == 0:
  computerChoice = rock
  print(f"Computer chooses {computerChoice}")

elif computerChoice == 1:
  computerChoice = paper
  print(f"Computer chooses {computerChoice}")

elif computerChoice == 2:
  computerChoice = scissors
  print(f"Computer chooses {computerChoice}")

if userChoice==computerChoice:
  print("Draw")
elif userChoice==1 and computerChoice==0:
  print("You win")

elif userChoice==2 and computerChoice==1:
  print("You win")

elif userChoice==0 and computerChoice==2:
  print("You win")

else:
  print("You lose")
