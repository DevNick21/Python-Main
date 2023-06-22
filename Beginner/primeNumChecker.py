# Write your code below this line 👇
def prime_checker(number):
    if number != 2 and number != 3 and number % 3 != 0 and number % 2 != 0:
        print("Prime")
    else:
        print("Not Prime")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
