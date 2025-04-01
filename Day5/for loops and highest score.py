# range function with for loop

# for i in range(1, 10):
#     print(i)  # it will print 1 to 9 it excludes last here 10
# for i in range(1,10, 3):
#     print(i)  # step up by 3

# add number between 1 to 100
addition = 0
for i in range(1, 101):
    addition += i
print(f"sum of ints between 1 to 100 is: {addition}")