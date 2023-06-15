# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
height = 0
num = 0
for ave in student_heights:
    height = height + ave
for ave in student_heights:
    num += 1
print(round(height/num))
