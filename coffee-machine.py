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
    
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        # check if resources are sufficient
        if menu.resources['water'] < menu.MENU[choice]['ingredients']['water']:
            print(f'Sorry there is not enough water to make your ${choice}')
        elif menu.resources['coffee'] < menu.MENU[choice]['ingredients']['coffee']:
            print(f'Sorry there is not enough coffee to make your ${choice}')
        elif choice == 'latte' or choice == 'cappuccino':
            if menu.resources['milk'] < menu.MENU[choice]['ingredients']['milk']:
                print(f'Sorry there is not enough milk to make your ${choice}')
            else:
                # process coins
                print('Please insert coins')
                quarters = int(input('How many quarters?: ')) * 0.25
                dimes = int(input('How many dimes?: ')) * 0.10
                nickles = int(input('How many nickles?: ')) * 0.05
                pennies = int(input('How many pennies?: ')) * 0.01
                total_money = quarters + dimes + nickles + pennies 
                if total_money < menu.MENU[choice]['cost']:
                  print(f'Sorry that is not enough money for your ${choice}')
                elif total_money >= menu.MENU[choice]['cost']:
                  menu.MENUresources['money'] += menu.MENU[choice]['cost']
                  change = round(total_money - menu.MENU[choice]['cost'], 2)
                  print(f'Here is ${change} in change')
                  print(f'Here is your {choice} ☕. Enjoy!')
                  menu.resources['water'] -= menu.MENU[choice]['ingredients']['water']
                  menu.resources['coffee'] -= menu.MENU[choice]['ingredients']['coffee']
                  if choice == 'latte' or choice == 'cappuccino':
                    menu.resources['milk'] -= menu.MENU[choice]['ingredients']['milk']
                  
        else:
          # process coins
          print('Please insert coins')
          quarters = int(input('How many quarters?: ')) * 0.25
          dimes = int(input('How many dimes?: ')) * 0.10
          nickles = int(input('How many nickles?: ')) * 0.05
          pennies = int(input('How many pennies?: ')) * 0.01
          total_money = quarters + dimes + nickles + pennies 
          if total_money < menu.MENU[choice]['cost']:
            print(f'Sorry that is not enough money for your ${choice}')
          elif total_money >= menu.MENU[choice]['cost']:
            menu.resources['money'] += menu.MENU[choice]['cost']
            change = round(total_money - menu.MENU[choice]['cost'], 2)
            print(f'Here is ${change} in change')
            print(f'Here is your {choice} ☕. Enjoy!')
            menu.resources['water'] -= menu.MENU[choice]['ingredients']['water']
            menu.resources['coffee'] -= menu.MENU[choice]['ingredients']['coffee']
            if choice == 'latte' or choice == 'cappuccino':
              menu.resources['milk'] -= menu.MENU[choice]['ingredients']['milk']
            
    
    # check resources for drink to see if we can make them
    