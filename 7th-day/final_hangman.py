words_list = [
    "apple", "banana", "mango", "grapes", "orange", "watermelon","pineapple", "papaya", "guava",
    "strawberry", "cherry", "blueberry", "blackberry", "raspberry""lemon", "lime", "coconut",
    "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
    ]
import random
from hangman_art import hangman_logo
from hangman_word_list import word_list
chosen_word=random.choice(word_list)
chosen_word_length=len(chosen_word)

end_of_game=False
lives=6






from hangman_art import stages
print(stages)
