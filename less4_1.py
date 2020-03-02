def salary():
    try:
        time = float(input("Введите кол-во выработанных часов: "))
        ante = float(input("Введите ставку сотрудника(в час): "))
        bonus = float(input("Введите премию сотрудника: "))
        salary = time * ante + bonus
        print('Заработная плата сотрудника:', salary)
    except ValueError:
        return print("Это не число!")


salary()
