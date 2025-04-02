# step-1 : select a word from a list and assign it to a variable
import random

word_list = ["cat", "dog", "cow", "Elephant"]
chosen_word = random.choice(word_list)
print(chosen_word)

# to do replace chosen word letters with _
placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

# step-2 : ask the user to guess a word and assign it  to a variable and convert it to a lower case
guess = input("guess a letter: ").lower()
# print(guess)

# create display in which guessed correct letters will be put at the blank
display = ""
# print(display)
# step-3 : check if the guessed letter exists in the chosen word
for letter in chosen_word:
    if letter == guess:
        # print("Right")
        display += letter
    else:
        # print("Wrong")
        display += "_"
print(display)
