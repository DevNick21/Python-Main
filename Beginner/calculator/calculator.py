# Calculator Main
from art import logo
# Add


def add(n1, n2):
    """Adds two inputs and returns the result"""
    return n1 + n2

# Subtract


def subtract(n1, n2):
    """Subtracts two inputs and returns the result"""
    return n1 - n2

# Multiply


def multiply(n1, n2):
    """Multiplies two inputs and returns the result"""
    return n1 * n2

# Divide


def divide(n1, n2):
    """Divides two inputs and returns the result"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    do_again = True

    while do_again:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calc = operations[operation_symbol]

        result = calc(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        another_operation = input(
            f"Type 'y' to continue calculation with {result} or type 'n' to start a new calculation.: ")

        if another_operation == 'y':
            num1 = result
        else:
            do_again = False
            calculator()


calculator()
