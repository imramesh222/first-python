import random
words_list = [
    "apple", "banana", "mango", "grapes", "orange", "watermelon","pineapple", "papaya", "guava",
    "strawberry", "cherry", "blueberry", "blackberry", "raspberry""lemon", "lime", "coconut",
    "avocado", "pomegranate", "peach", "pear", "plum", "apricot"
    ]
chosen_word = random.choice(words_list)
print(f"The chosen word is {chosen_word}")

display = ["_" for _ in range(len(chosen_word))]
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
