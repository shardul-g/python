# 0 for rock , 1 for paper, 2 for scissors
import random
user_input = int(input("0 for rock , 1 for paper, 2 for scissors:\n"))
computer_choice = random.randint(0, 2)

print(f"computer choose: {computer_choice}")
if 3 <= user_input <= 0:
    print("Invalid number You loose")
elif user_input == 0 and computer_choice == 2:
    print("you won")
elif computer_choice == 0 and user_input == 2:
    print("you loose")
elif computer_choice > user_input:
    print("you loose")
elif user_input > computer_choice:
    print("you win")
elif user_input == computer_choice:
    print("Its a draw")
