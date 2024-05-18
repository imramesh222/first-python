# list = ['larry', 'curly', 'moe']
# if 'moe' in list:
#     print('yes') 
import random
print("Wewlcome to Hangman words game\n")

words_list = ["apple", "banana", "mango", "grapes", "orange", "watermelon", "pineapple", "papaya", "guava", "strawberry", "cherry", "blueberry", "blackberry", "raspberry", "lemon", "lime", "coconut", "avocado", "pomegranate", "peach", "pear", "plum", "apricot"]
random_word=random.choice(words_list)

def generate_blanks(random_word):
  word=random_word.split()
  