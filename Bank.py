#---------------------------------подготовка--------------------------------
def balance_plus(balance: float, amount: float):
    if amount < 0:
        print("Введено некорректное число" + "\n")
        return balance
    else:
        balance+= amount
        print(f"> Вы внесли {amount}. Ваш баланс: {balance} рублей" + "\n")
        confirmation=int(input("Введите 1 чтобы продолжить, 2 чтобы отменить операцию"))
        if confirmation==2:
          balance -= amount
        return balance

def balance_minus(balance: float, amount: float):
    if amount < 0:
        print("Введено некорректное число" + "\n")
    elif amount > balance:
        print("Недостаточно средств")
    else:
        balance-= amount
        print(f"> Вы cняли {amount} Ваш баланс: {balance} рублей" + "\n")
        confirmation=int(input("Введите3 1 чтобы продолжить, 2 чтобы отменить операцию"))
        if confirmation==2:
          balance += amount
    return balance
i=0
balance = 0
amount=0
confirmation=0
#---------------------------------код--------------------------------
while i == 0:
    print("Меню"+ "\n" + "1 - показать баланс"+ "\n" + "2 - внести сумму"+"\n"+ "3 - снять сумму"+"\n"+ "4 -выйти из программы")
    action = input("Выберите действие: ")
    if action == "1":
        print(f"> Ваш баланс: {balance} рублей" + "\n")
    elif action == "2":
        amount = float(input("Введите сумму: "))
        balance = balance_plus(balance, amount)

    elif action == "3":
        amount = float(input("Введите сумму: "))
        balance = balance_minus(balance, amount)

    elif action == "4":
        print("Выход из программы...")
        i = 1
    else:
        print("Некорректная операция" +"\n")
