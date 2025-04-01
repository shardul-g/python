import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to python password generator")
random_letter = int(input("How many letters do you want in password ?\n"))
randon_number = int(input("How many numbers do you want in password?\n"))
random_symbol = int(input("How many symbols do you want in password?\n"))

# password = ""
# for char in range(0, random_letter):
#     password += random.choice(letter)
# for char in range(0, randon_number):
#     password += random.choice(number)
# for char in range(0,random_symbol):
#     password += random.choice(symbols)
# print(password)

password_list = []
for char in range(0, random_letter):
    password_list.append(random.choice(letter))
for char in range(0, randon_number):
    password_list.append(random.choice(number))
for char in range(0, random_symbol):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)   # to shuffle items in list
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"your generated password is : {password}")
