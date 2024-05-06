import random

rock="✊"
paper="📃"
scissors="✂"

user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))

if user_choice==0:
  user_choice=rock
  print(f"You chose {user_choice}")
elif user_choice==1:
  user_choice=paper
  print(f"You chose {user_choice}")
elif user_choice==2:
  user_choice=scissors
  print(f"You chose {user_choice}")
else:
  print("Invalid choice")
  exit()

computer_choice=random.randint(0,2)

if computer_choice == 0:
    computer_choice = rock
    print(f"Computer chooses {computer_choice}")
elif computer_choice == 1:
    computer_choice = paper
    print(f"Computer chooses {computer_choice}")
else:
    computer_choice = scissors
    print(f"Computer chooses {computer_choice}")

if user_choice==computer_choice:
  print("Draw")
elif user_choice==0 and computer_choice==2:
  print("You win")
elif user_choice==1 and computer_choice==0:
  print("You win")
elif user_choice==2 and computer_choice==1:
  print("You win")
else:
  print("Computer wins")
