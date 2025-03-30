# fruits = ["apple", "banana"]
# veggies = ["tomato", "potato"]
# combi = [fruits, veggies]
# print(combi)  # [['apple', 'banana'], ['tomato', 'potato']]
# print(len(combi))  # 2
# import random
#
# print(random.choice(combi)) #['apple', 'banana'] or ["tomato", "potato"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits)
# fruits[-1] = "Melons"
# print(fruits)
# fruits.append("Lemons")
# print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) # Kale
print(dirty_dozen[1][4]) # Potatoes
print(dirty_dozen[0][4])    #Peaches