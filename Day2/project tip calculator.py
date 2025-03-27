print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill ?\n$"))   # total bil amount
tip_to_give = float(input("how much tip would you like to give ? 10 20 \n"))  # percentage of total bill to give
tip = (total_bill * (tip_to_give / 100))
total_bill = total_bill + tip
number_of_people = int(input("how many people to split the bill?\n"))
per_head_pay = round((total_bill / number_of_people), 2)
print(f"Each person should pay : {per_head_pay}")
