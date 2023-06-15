import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
user = int(
    input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS\n"))

computer = random.randint(0, 2)

rps = [rock, paper, scissors]

print(f"{rps[computer]}\nComputer chose: \n {rps[user]} You chose")

if computer == user:
    print("It was a draw")
elif computer == 0 and user == 1:
    print("You win")
elif computer == 0 and user == 2:
    print("You lose")
elif computer == 1 and user == 0:
    print("You lose")
elif computer == 1 and user == 2:
    print("You win")
elif computer == 2 and user == 0:
    print("You win")
elif computer == 2 and user == 1:
    print("You lose")
else:
    print("Something went wrong")
