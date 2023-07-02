# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo


# Progran Intro
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

num = []

for x in range(1, 101):
    num.append(x)

difficulty_count = 0

random_num = random.choice(num)


def make_a_guess():
    """It allows the user make a guess and takes the guess against the random_num, then print a response relative to the input and changes difficulty_count"""
    global difficulty_count
    user_input = int(input("Make a guess: "))
    if user_input == random_num:
        difficulty_count = 0
        print("You Got it right")
    elif user_input > random_num:
        difficulty_count -= 1
        print("Too high.\nGuess Again.")
        print(
            f"You have {difficulty_count} attempts remaining to guess the number")
    elif user_input < random_num:
        difficulty_count -= 1
        print("Too Low\nGuess Again.")
        print(
            f"You have {difficulty_count} attempts remaining to guess the number")


if difficulty == "easy":
    difficulty_count = 10
    while difficulty_count > 0:
        make_a_guess()
elif difficulty == "hard":
    difficulty_count = 5
    while difficulty_count > 0:
        make_a_guess()

if difficulty_count == 0:
    print(f"You are out of attempts")
