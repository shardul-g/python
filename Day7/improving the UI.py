# step-1 : select a word from a list and assign it to a variable
import random
import hangman_list
import hangman_art
# setting the number of lives to 6
lives = 6
word_list = hangman_list.animals
chosen_word = random.choice(word_list)
# stages
hangman_stages = hangman_art.stages

# print(chosen_word)
correct_letters = []
# to do replace chosen word letters with _
placeholder = ""
for i in chosen_word:
    placeholder += "_"
print(f"letter to guess : {placeholder}")

# step-2 : ask the user to guess a word and assign it  to a variable and convert it to a lower case
game_over = False
while not game_over:

    guess = input("guess a letter: ").lower()
    # print(guess)

    # if letter is guessed already let the user know, and deduct no lives
    if guess in correct_letters:
        print(f"*****You have already guessed {guess}: No lives deducted, Try again !*****")

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
            print("*****You Loose !*****")
            print(f"**** chosen word was: {chosen_word} ****")
        print(f"***** > {guess} is not in the chosen word,loosed a life ! try again*****")

    print(f"***** lives remaining : {lives} / 6 *****")
    if "_" not in display:
        game_over = True
        print("*****You Won !*****")

    # printing the stage as per ascii
    print(hangman_stages[lives])
