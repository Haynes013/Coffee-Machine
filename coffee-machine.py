import menu
import time
# power turns the coffee machine on and off.
power = True

while power:
    # prompt user by asking what would you like
    choice = input("What would you like to drink? \n(espresso/latte/cappuccino): ").lower()
    
    # The "off" secret word shut down the machine
    if choice == 'off':
        print('Powering off in')
        time.sleep(2)
        print('3')
        time.sleep(2)
        print('2')
        time.sleep(2) 
        print('1')
        time.sleep(2) 
        print('GoodBye')
        power = False
        
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif choice == 'report':
        print(menu.resources)
        