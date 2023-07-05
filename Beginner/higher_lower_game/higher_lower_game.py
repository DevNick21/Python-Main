import random
from game_data import data
from art import logo
from art import vs

# Program Intro

score = 0
isGameOver = False


def entity():
    """Randomly accesses any dictionary containing the name, follower count, description and country"""
    random_entity = data[random.randint(0, 49)]

    # Accessing the entity bringing out the the data
    name = random_entity["name"]
    followers = random_entity["follower_count"]
    description = random_entity["description"]
    location = random_entity["country"]

# Returning the accessed data in variables as a list
    return [name, followers, description, location]


# Generating the first inputs
first_account_A = entity()
first_account_B = entity()
# Check for rare cases where the computer generates two identical accounts
if first_account_A == first_account_B:
    first_account_B = entity()


def main_game(insta_A, insta_B):
    """Main game function, collect two inputs and stores it in a variable 'list_a and list_b', then while isGameOver is False,
    it executes the game and compares the user input with the checker function check, which is the computer indirectly playing
    the game and comparing the answer with the user but using direct information from the backend, if incorrect, isGameOver becomes
    True and the while loop comes to and end and also it does execute the function again """
    list_a = insta_A
    list_b = insta_B
    global isGameOver
    global rareCase
    global score
    while not isGameOver:
        # Check for rare cases where the computer generates two identical accounts within the loop
        if insta_A == insta_B:
            insta_B = entity()
        print(logo)
        # Printing the neccessary information for the user
        print(
            f"Compare A: {insta_A[0]}, a {insta_A[2]}, from {insta_A[3]}")
        print(vs)

        print(
            f"Compare B: {insta_B[0]}, a {insta_B[2]}, from {insta_B[3]}")

        def checker():
            """Checks the follower count and find the higher and lower then returns A or B respectively"""
            if insta_A[1] > insta_B[1]:
                return "A"
            elif insta_A[1] < insta_B[1]:
                return "B"

        user = str(input("Who has more followers? Type 'A' or 'B': ").upper())

# Checking if the user input is equal to the computer's backend check
        if user == "A" and checker() == "A":
            not isGameOver
            score += 1
            print(f"You are Right!. Current Score: {score}")
            main_game(insta_A=list_a, insta_B=entity())
        elif user == "B" and checker() == "B":
            not isGameOver
            score += 1
            print(f"You are Right!. Current Score: {score}")
            main_game(insta_A=list_b, insta_B=entity())
        else:
            print(f"Sorry, That's wrong. Final Score: {score}")
            isGameOver = True


# Indirect beginning of the game, which checks if isGameOver is equal to False to avoid game loop and then triggers function to begin game
if isGameOver == False:
    main_game(insta_A=first_account_A, insta_B=first_account_B)
