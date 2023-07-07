def ChangeInDollars():
    print("dites svp votre nombre de chaque piece")
    quarters = int(input("Quarters: "))
    Dimes = int(input("Dimes: "))
    nickels = int(input("Nickel: "))
    pennies = int(input("pennies: "))
    total = quarters * .25 + Dimes * .10 + nickels* .05 + pennies * .01 #pas compris pk .25...
    print()
    print("The total value of ur change is {}" .format(total))
    question = input('do you want de change in eur ')
    question.upper()
    if question == 'YES':
        print("the change from to usd to eur is 1usd = 0.91eur")
        change = total * 0.91
        print(change)

        
ChangeInDollars()
