student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    name = student_scores[key]
    if name >= 91:
        student_grades[key] = "Outstanding"
    elif name >= 81 and name < 90:
        student_grades[key] = "Exceeds Expectation"
    elif name >= 71 and name < 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)

travel_log = {
    "France": {"cites_visited": ["Paris", "Lille", "Dijon"], "total_visits": 22},
    "Germany": {"cites_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
}
travel_lug = [
    {"country": "France",
     "cites_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 22},
    {"country": "Germany",
     "cites_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 12},
]
