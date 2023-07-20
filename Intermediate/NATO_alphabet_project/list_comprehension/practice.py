# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # Do Not Change the code above

# # Write you 1 line code below:
# squared_numbers = [num * num for num in numbers]
# # Write your code above:

# print(squared_numbers)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # Do Not Change the code above

# # Write you 1 line code below:
# result = [num for num in numbers if num % 2 == 0]
# # Write your code above:

# print(result)


# with open("NATO_alphabet_project/list_comprehension/day_26_3_exercise_files/file1.txt") as file_one:
#     first_list_with = file_one.readlines()
# first_list = [num.strip() for num in first_list_with]

# with open("NATO_alphabet_project/list_comprehension/day_26_3_exercise_files/file2.txt") as file_one:
#     second_list_with = file_one.readlines()
# second_list = [num.strip() for num in second_list_with]


# result = [int(num) for num in first_list if num in second_list]

# # Write your code above 👆

# print(result)


# import random

# name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {student: random.randint(1, 100) for student in name}

# passed_students = {student: score for (
#     student, score) in student_scores.items() if score >= 60}


# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# # Write your code below:
# sentence_list = sentence.split()
# results = {word: len(word) for word in sentence_list}


# print(results)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

# print(weather_f)


import pandas

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_df = pandas.DataFrame(student_dict)

nato_dict = {index: row for (index, row) in student_df.iterrows()}


# for (index, row) in student_df.iterrows():
#     print(row.score)
print(nato_dict)
