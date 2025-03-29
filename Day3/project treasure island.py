print("Welcome to treasure Island.\nYour mission is to find the treasure.")
choice1 = input("Which door you want to go? Left or Right: \n").lower()
if choice1 == "left":
    choice2 = input("You want to swin or wait for a boat ? swim or wait: \n").lower()
    if choice2 == "wait":
        choice3 = input("Which door you want to go? Red, Blue, Yellow:\n").lower()
        if choice3 == "blue":
            print("Fire inside room!! Game over!!")
        elif choice3 == "red":
            print("Tiger inside room. Game over!!")
        elif choice3 == "yellow":
            print("Found treasure. You won!!")
        else:
            print("You selected a door which does not exists!!, Game over!!")
    else:
        print("Drowned in water! Game over!!")
else:
    print("You selected wrong door. Game Over!!")
