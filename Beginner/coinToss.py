import random
# import my_module
user = str(input("Heads or Tails\n")).lower()
computer = random.randint(0, 1)
if computer == 0:
    print("Computer: Heads")
else:
    print("Computer: Tails")

if user == "heads" and computer == 0:
    print("You win! It was Heads")
elif user == "heads" and computer == 1:
    print("You lost :( It was Tails")
elif user == "tails" and computer == 1:
    print("You win! It was Tails")
elif user == "tails" and computer == 0:
    print("You lost :( It was Heads")
else:
    print("INVALID, Restart please")
