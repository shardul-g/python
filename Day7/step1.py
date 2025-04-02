# step-1 : select a word from a list and assign it to a variable
import random

word_list = ["cat", "dog", "cow"]
chosen_word = random.choice(word_list)
print(chosen_word)

# step-2 : ask the user to guess a word and assign it  to a variable and convert it to a lower case
guess = input("guess a letter: ").lower()
print(guess)

# step-3 : check if the guessed letter exists in the chosen word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
