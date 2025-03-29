print("Welcome to python pizza delivery!")
size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")

# approach 1 but errors are not handled in this correctly
bill = 0
# if size == "S":
#     bill += 15
#     if pepperoni == "Y":
#         bill += 2
# elif size == "M":
#     bill += 20
#     if pepperoni == "Y":
#         bill += 3
# elif size == "L":
#     bill += 25
#     if pepperoni == "Y":
#         bill += 3
# else:
#     print("You enter wrong input")
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your total bill is: ${bill}")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You enter wrong input")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: {bill}")
