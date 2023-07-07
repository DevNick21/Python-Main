from data import MENU
from data import resources

money = 0

machine_on = True

while machine_on == True:
    coffee_esp = MENU["espresso"]
    coffee_lat = MENU["latte"]
    coffee_cap = MENU["cappuccino"]

    esp_ingred = coffee_esp["ingredients"]
    lat_ingred = coffee_lat["ingredients"]
    cap_ingred = coffee_cap["ingredients"]

    total_water = resources["water"]
    total_milk = resources["milk"]
    total_coffee = resources["coffee"]

    user = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    if user == "espresso" or user == "latte" or user == "cappuccino":
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        money_quarters = quarters * 0.25
        money_dimes = dimes * 0.10
        money_nickles = nickles * 0.05
        money_penny = pennies * 0.01

        total_user_money = money_quarters + money_dimes + money_nickles + money_penny
    elif user == "report":
        print(
            f"Water: {total_water}\nMilk: {total_milk}\nCoffee: {total_coffee}\nMoney: {money}")
    elif user == "off":
        machine_on = False
    else:
        print("Enter a valid command")

    if user == "espresso":
        if total_user_money < coffee_esp["cost"]:
            print("Sorry that's not enough money. Money Refunded")
        elif esp_ingred["water"] > total_water:
            print("Sorry, there's not enough water")
        elif esp_ingred["coffee"] > total_coffee:
            print("Sorry, there's not enough coffee")
        else:
            total_water -= 50
            total_coffee -= 18
            money += 1.5
            print(
                f"Here's your change ${total_user_money - coffee_esp['cost']}.")
            print("Here is your espresso ☕. Enjoy!")
    elif user == "latte":
        if total_user_money < coffee_lat["cost"]:
            print("Sorry that's not enough money. Money Refunded")
        elif lat_ingred["water"] > total_water:
            print("Sorry, there's not enough water")
        elif lat_ingred["coffee"] > total_coffee:
            print("Sorry, there's not enough coffee")
        elif lat_ingred["milk"] > total_milk:
            print("Sorry, there's not enough milk")
        else:
            total_water -= 200
            total_coffee -= 24
            total_milk -= 150
            money += 2.5
            print(
                f"Here's your change ${total_user_money - coffee_lat['cost']}.")
            print("Here is your latte ☕. Enjoy!")
    elif user == "cappuccino":
        if total_user_money < coffee_cap["cost"]:
            print("Sorry that's not enough money. Money Refunded")
        elif cap_ingred["water"] > total_water:
            print("Sorry, there's not enough water")
        elif cap_ingred["coffee"] > total_coffee:
            print("Sorry, there's not enough coffee")
        elif cap_ingred["milk"] > total_milk:
            print("Sorry, there's not enough milk")
        else:
            total_water -= 250
            total_coffee -= 24
            total_milk -= 100
            money += 3.0
            print(
                f"Here's your change ${total_user_money - coffee_lat['cost']}.")
            print("Here is your cappuccino ☕. Enjoy!")
