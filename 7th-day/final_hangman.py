words_list = [
    "apple", "banana", "mango", "grapes", "orange", "watermelon","pineapple", "papaya", "guava",
    "strawberry", "cherry", "blueberry", "blackberry", "raspberry""lemon", "lime", "coconut",
    "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
    ]
import random
from hangman_word_list import Word_list
chosen_word=random.choice(words_list)
chosen_word_length=len(chosen_word)

end_of_game=False
lives=6






from hangman_art import HANGMANPICS
print(HANGMANPICS)
