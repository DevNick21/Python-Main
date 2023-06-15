import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
namesLen = len(names)
list_len = namesLen - 1
random_listnum = random.randint(0, list_len)
payer = names[random_listnum]
print(f"{payer} is going to buy the meal today!")
