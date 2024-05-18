# import random

# def display_blanks(word, correct_guesses):
#     return ' '.join([letter if letter in correct_guesses else '_' for letter in word])

# def main():
#     print("Welcome to Hangman words game\n")

#     words_list = [
#         "apple", "banana", "mango", "grapes", "orange", "watermelon", "pineapple", "papaya", "guava",
#         "strawberry", "cherry", "blueberry", "blackberry", "raspberry", "lemon", "lime", "coconut",
#         "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
#     ]
    
#     random_word = random.choice(words_list)
#     correct_guesses = set()
#     wrong_guesses = set()
#     attempts = 6

#     while attempts > 0:
#         print(f"\nWord: {display_blanks(random_word, correct_guesses)}")
#         print(f"Wrong guesses: {', '.join(wrong_guesses)}")
#         print(f"Attempts left: {attempts}")

#         guess = input("Guess a letter: ").lower()
        
#         if guess in correct_guesses or guess in wrong_guesses:
#             print("You already guessed that letter. Try again.")
#             continue
        
#         if guess in random_word:
#             correct_guesses.add(guess)
#             print("Good guess!")
#         else:
#             wrong_guesses.add(guess)
#             attempts -= 1
#             print("Wrong guess!")
        
#         if all(letter in correct_guesses for letter in random_word):
#             print(f"\nCongratulations! You guessed the word: {random_word}")
#             break
#     else:
#         print(f"\nSorry, you've run out of attempts. The word was: {random_word}")

# if __name__ == "__main__":
#     main()

import random
words_list = [
    "apple", "banana", "mango", "grapes", "orange", "watermelon","pineapple", "papaya", "guava",
    "strawberry", "cherry", "blueberry", "blackberry", "raspberry""lemon", "lime", "coconut",
    "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
    ]
chosen_word=random.choice(words_list)
print(f"the chosen word is {chosen_word}")
word_length=len(chosen_word)
display=[]
for _ in range(word_length):
  display+="_"
print(display)
end_of_game=False
while not end_of_game:
    guess=input("Guess a letter: ").lower()
    for position in range(word_length):
        letter=chosen_word[position]
        print(f"Current position: {position}\n Current letter:{letter}\n Gussed letter:{letter}")
        if letter==guess:
            display[position]=letter

    print(f"{' '.join(display)}") 
    if "_" not in display:
        end_of_game=True
        print("You win!")
