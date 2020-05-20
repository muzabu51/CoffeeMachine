# Cappuccino
Cap_reqd_water = 200  # ml
Cap_reqd_milk = 100  # ml
Cap_reqd_beans = 12  # g
Cap_cost = 6  # $
# Espresso
Esp_reqd_water = 250  # ml
Esp_reqd_milk = 0  # ml
Esp_reqd_beans = 16  # g
Esp_cost = 4  # $
# Latte
Lat_reqd_water = 350  # ml
Lat_reqd_milk = 75  # ml
Lat_reqd_beans = 20  # g
Lat_cost = 7  # $
# available quantities
qty_water = 400
qty_milk = 540
qty_beans = 120
no_of_cups = 9
money = 550


def fill():
    global qty_water
    global qty_milk
    global qty_beans
    global no_of_cups
    global money
    qty_water += int(input('Write how many ml of water do you want to add: '))
    qty_milk += int(input('Write how many ml of milk do you want to add: '))
    qty_beans += int(input('Write how many grams of coffee beans do you want to add: '))
    no_of_cups += int(input('Write how many ml disposable cups of coffee do you want to add: '))
    print()


def take():
    global money
    print(f'I gave you ${money}')
    money = 0
    print()


def output():
    print('The coffee machine has:')
    print(f'{qty_water} of water')
    print(f'{qty_milk} of milk')
    print(f'{qty_beans} of coffee beans')
    print(f'{no_of_cups} of disposable cups')
    print(f'${money} of money')
    print()


def msg(txt):
    print(f'Sorry, not enough {txt}!')


def buy():
    inp = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: , back - to main menu: ')
    global qty_water
    global qty_milk
    global qty_beans
    global no_of_cups
    global money
    possibility = 1
    if inp == '1':
        if qty_water < Esp_reqd_water:
            msg('water')
            possibility = 0
            print()
        elif qty_milk < Esp_reqd_milk:
            msg('milk')
            possibility = 0
            print()
        elif qty_beans < Esp_reqd_beans:
            msg('coffee beans')
            possibility = 0
            print()
        elif no_of_cups == 0:
            possibility = 0
            msg('disposable cups')
        if possibility:
            qty_water -= Esp_reqd_water
            qty_milk -= Esp_reqd_milk
            qty_beans -= Esp_reqd_beans
            no_of_cups -= 1
            money += Esp_cost
            print('I have enough resources, making you a coffee!')
        print()
    elif inp == '2':
        if qty_water < Lat_reqd_water:
            msg('water')
            possibility = 0
            print()
        elif qty_milk < Lat_reqd_milk:
            msg('milk')
            possibility = 0
            print()
        elif qty_beans < Lat_reqd_beans:
            msg('coffee beans')
            possibility = 0
            print()
        elif no_of_cups == 0:
            possibility = 0
            msg('disposable cups')
        if possibility:
            qty_water -= Lat_reqd_water
            qty_milk -= Lat_reqd_milk
            qty_beans -= Lat_reqd_beans
            no_of_cups -= 1
            money += Lat_cost
            print('I have enough resources, making you a coffee!')
        print()
    elif inp == '3':
        if qty_water < Cap_reqd_water:
            msg('water')
            possibility = 0
            print()
        elif qty_milk < Cap_reqd_milk:
            msg('milk')
            possibility = 0
            print()
        elif qty_beans < Cap_reqd_beans:
            msg('coffee beans')
            possibility = 0
            print()
        elif no_of_cups == 0:
            possibility = 0
            msg('disposable cups')
        if possibility:
            qty_water -= Cap_reqd_water
            qty_milk -= Cap_reqd_milk
            qty_beans -= Cap_reqd_beans
            no_of_cups -= 1
            money += Cap_cost
            print('I have enough resources, making you a coffee!')
        print()
    elif inp == 'back':
        main()


def main():
    inp = input('Write action (buy, fill, take, remaining, exit): ')
    if inp == 'buy':
        print()
        buy()
    elif inp == 'fill':
        print()
        fill()
    elif inp == 'take':
        print()
        take()
    elif inp == 'remaining':
        print()
        output()
    elif inp == 'exit':
        return inp


while True:
    out = main()
    if out == 'exit':
        break
