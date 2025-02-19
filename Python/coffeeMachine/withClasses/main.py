from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True
while on:
    order = input(f"What would you like to order? Options are {menu.get_items()}: ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        on = False
        break
    else:
        order = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(order):
            money_machine.make_payment(order.cost)
            coffee_maker.make_coffee(order)