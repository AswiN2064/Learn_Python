# same of Day_015 project

# here you need to get hands on practice about classes and objects

# menu.py, money.py , money_machine.py, coffee maker.py
# was provided
# in main.py, you can get hint about what are the classes we are going to use.

# refer each py file to see what each class is doing.


# 1 -> Print report
# 2 -> is resources sufficient
# 3 -> Process coins
# 4 -> check transaction successfull
# 5 -> make coffee

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1 -> Print report
machine_money = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
# menu_item = MenuItem()

while is_on:
    options = menu.get_items()
    selected_option = input(f"What should you need from ({options}) ? :")
    if selected_option == "off":
        is_on = False
    # 1 -> Print report
    elif selected_option == "report":
        coffee_maker.report()
        machine_money.report()
    # 2 -> is resources sufficient
    else:
        drink = menu.find_drink(selected_option)        # return object type
        if coffee_maker.is_resource_sufficient(drink):
            # 3 -> Process coins, # 4 -> check transaction successfull
            if machine_money.make_payment(drink.cost):
                # 5 -> make coffee
                coffee_maker.make_coffee(drink)




# print(menu.find_drink("latte"))
# print(menu_item.name("latte"))
# print(coffee_maker.is_resource_sufficient("latte"))


'''
output:
-------

What should you need from (latte/espresso/cappuccino/) ? :latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
What should you need from (latte/espresso/cappuccino/) ? :report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
What should you need from (latte/espresso/cappuccino/) ? :cappuccino
Sorry there is not enough water.
What should you need from (latte/espresso/cappuccino/) ? :espresso
Please insert coins.
How many quarters?: 15
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $2.25 in change.
Here is your espresso ☕️. Enjoy!
What should you need from (latte/espresso/cappuccino/) ? :report
Water: 50ml
Milk: 50ml
Coffee: 58g
Money: $4.0
What should you need from (latte/espresso/cappuccino/) ? :espresso
Please insert coins.
How many quarters?: 5 
How many dimes?: 0
How many nickles?: 00
How many pennies?: 0
Sorry that's not enough money. Money refunded.
What should you need from (latte/espresso/cappuccino/) ? :espresso
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $1.0 in change.
Here is your espresso ☕️. Enjoy!
What should you need from (latte/espresso/cappuccino/) ? :espresso
Sorry there is not enough water.
What should you need from (latte/espresso/cappuccino/) ? :report
Water: 0ml
Milk: 50ml
Coffee: 40g
Money: $5.5
What should you need from (latte/espresso/cappuccino/) ? :off
'''
