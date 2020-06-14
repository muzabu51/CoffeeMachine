class CoffeeMachine:
    # Cappuccino
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}

    # Espresso
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}

    # Latte
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}

    def __init__(self, water, milk, beans, cups, money, state='main'):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = state
        self.possibility = 1

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n '))
        self.milk += int(input('Write how many ml of milk do you want to add:\n '))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n '))
        self.cups += int(input('Write how many ml disposable cups of coffee do you want to add:\n '))
        self.possibility = 1
        print()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        print()

    def output(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')
        print()

    def msg(self, txt):
        print(f'Sorry, not enough {txt}!')

    def buycheck(self, coffee):
        if self.water < coffee['water']:
            self.msg('water')
            self.possibility = 0
        elif self.milk < coffee['milk']:
            self.msg('milk')
            self.possibility = 0
        elif self.beans < coffee['beans']:
            self.msg('coffee beans')
            self.possibility = 0
        elif self.cups == 0:
            self.possibility = 0
            self.msg('disposable cups')

    def checkpos(self, coffee):
        if self.possibility:
            self.water -= coffee['water']
            self.milk -= coffee['milk']
            self.beans -= coffee['beans']
            self.cups -= 1
            self.money += coffee['cost']
            print('I have enough resources, making you a coffee!')
        print()

    def buy(self):
        inp = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n ')
        if inp == '1':
            self.buycheck(self.espresso)
            self.checkpos(self.espresso)
        elif inp == '2':
            self.buycheck(self.latte)
            self.checkpos(self.latte)
        elif inp == '3':
            self.buycheck(self.cappuccino)
            self.checkpos(self.cappuccino)
        elif inp == 'back':
            self.main()

    def main(self):
        inp = input('Write action (buy, fill, take, remaining, exit):\n ')
        if inp == 'buy':
            print()
            self.buy()
        elif inp == 'fill':
            print()
            self.fill()
        elif inp == 'take':
            print()
            self.take()
        elif inp == 'remaining':
            print()
            self.output()
        elif inp == 'exit':
            return inp


cm = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    out = cm.main()
    if out == 'exit':
        break
