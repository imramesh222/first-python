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


words_list = [
    "apple", "banana", "mango", "grapes", "orange", "watermelon""pineapple", "papaya", "guava",
    "strawberry", "cherry", "blueberry", "blackberry", "raspberry""lemon", "lime", "coconut",
    "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
    ]
import random

chosen_word=random.choice(words_list)
print(chosen_word)

guess=input("Guess a letter: ").lower()

for letter in chosen_word:
  if letter==guess:
    print("Right")
  else:
    print("Wrong")