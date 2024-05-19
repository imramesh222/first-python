words_list = [
    "apple", "banana", "mango", "grapes", "orange", "watermelon","pineapple", "papaya", "guava",
    "strawberry", "cherry", "blueberry", "blackberry", "raspberry""lemon", "lime", "coconut",
    "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
    ]
import random
from hangman_art import logo
from hangman_word_list import word_list
chosen_word=random.choice(word_list)
chosen_word_length=len(chosen_word)

end_of_game=False
lives=6




from hangman_art import logo,stages
print(logo)

#testing code
print(f'Passt, the solution is {chosen_word}.')


# create blanks
display=[]
for _ in range(chosen_word_length):
  display+="_"

while not end_of_game:
  guess=input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed {guess}")
  if guess in display:
    print(f"You've already guessed {guess}")
    continue

  for position in range(chosen_word_length):
    letter=chosen_word[position]
    print(f"Current position: {position}\n Current letter:{letter}\n Gussed letter:{letter}")
    if letter==guess:
      display[position]=letter
  if guess not in chosen_word:
    print(f"YOu guessed {guess}, that's not in word.You lose a life")
    lives-=1
    if lives==0:
      end_of_game=True
      print("You lose!")
     

  print(f"{' '.join(display)}") 
  if "_" not in display:
    end_of_game=True
    print("You win!")
  else:
    print("You lose!")  
    lives-=1
    if lives==0:
      end_of_game=True
      print("You lose!")
    else:
      print(f"You have {lives} lives left")
    print(f"{' '.join(stages[lives])}")






print(stages)
