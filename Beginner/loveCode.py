# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
Lname1 = name1.lower()
Lname2 = name2.lower()

totalName = Lname1 + Lname2

totalF = 0
totalS = 0

totalF += totalName.count("t")
totalF += totalName.count("r")
totalF += totalName.count("u")
totalF += totalName.count("e")

totalS += totalName.count("l")
totalS += totalName.count("o")
totalS += totalName.count("v")
totalS += totalName.count("e")

finalTotal = str(totalF) + str(totalS)
total = int(finalTotal)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
