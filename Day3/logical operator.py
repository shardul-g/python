# multiple if else statements in succession
print("Welcome to the roller coaster ")
height = int(input("Enter your height: \n"))
bill = 0
if height >= 120:
    print("You can ride :)")
    age = int(input("Enter your age : "))
    if age <= 12:
        bill = 5
        # print("please pay $5")
    elif age <= 18:
        bill = 7
        # print("please pay $7")
    elif age >= 45 and age <= 50:   # 45 <= age <=55
        print("Midlife crisis ride is free!! :)")
    else:
        bill = 12
        # print("please pay $12")
    wants_photo = input("Do you want to take a photo type y for yes and n for no.")
    if wants_photo == "y":
        bill += 3
    print(f"total bill is {bill}")
else:
    print("You need to grow taller to ride :(")
