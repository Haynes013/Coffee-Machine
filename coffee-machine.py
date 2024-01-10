import menu
# power turns the coffee machine on and off.
power = True

while power:
    # prompt user by asking what would you like
    choice = input("What would you like to drink? \n(espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        print('Powering off')
        power = False
    elif choice == 'report':
        print(menu.resources)