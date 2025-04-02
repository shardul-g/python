# step-1 : select a word from a list and assign it to a variable
import random
# setting the number of lives to 6
lives = 6
word_list = ["cat", "dog", "cow", "elephant"]
chosen_word = random.choice(word_list)
# stages
hangman_stages = [
    r"""
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    =======
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =======
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =======
    """,
    """
       ------
       |    |
       |
       |
       |
       |
    =======
    """
]

# Example of printing a stage
# print(hangman_stages[3])  # Prints the fourth stage from reversed list

# print(chosen_word)
correct_letters = []
# to do replace chosen word letters with _
placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(placeholder)

# step-2 : ask the user to guess a word and assign it  to a variable and convert it to a lower case
game_over = False
while not game_over:

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
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            # print("Wrong")
            display += "_"
    print(display)
    # reducing the number of lives for the wrong guess
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Loose")

    print(f"lives remaining : {lives}")
    if "_" not in display:
        game_over = True
        print("You Won !")

    # printing the stage as per ascii
    print(hangman_stages[lives])
