student_score = [100, 200, 250, 400, 500, 450]
# built-in function for sum
# total_score = sum(student_score)
# print(total_score)
# # using for loop
# total_sum = 0
# for score in student_score:
#     total_sum += score
# print(total_sum)
# to find the maximum number from list
max_score = max(student_score)
print(f"max score is {max_score}")
max_num = 0
for score in student_score:
    if score > max_num:
        max_num = score
print(f"max score is {max_num}")
