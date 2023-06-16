# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
EasyPassword = ""

for let in range(1, nr_letters + 1):
    rand_let = random.choice(letters)
    EasyPassword += rand_let
    # OR I CAN SAY
    # password += random.choice(letters)
    # SAME APPLIES FOR OTHERS

for sym in range(1, nr_symbols + 1):
    rand_sym = random.choice(symbols)
    EasyPassword += rand_sym
for numb in range(1, nr_numbers + 1):
    rand_numb = random.choice(numbers)
    EasyPassword += rand_numb

print(f"Your Easy Password is {EasyPassword}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
HardPassword_list = []
for let in range(1, nr_letters + 1):
    rand_let = random.choice(letters)
    HardPassword_list += rand_let
    # OR I CAN SAY
    # password += random.choice(letters)
    # SAME APPLIES FOR OTHERS

for sym in range(1, nr_symbols + 1):
    rand_sym = random.choice(symbols)
    HardPassword_list += rand_sym
for numb in range(1, nr_numbers + 1):
    rand_numb = random.choice(numbers)
    HardPassword_list += rand_numb
random.shuffle(HardPassword_list)
# print(HardPassword_list)

HardPassword = ""
for hard in HardPassword_list:
    HardPassword += hard
print(f"Your Hard Password is {HardPassword}")
