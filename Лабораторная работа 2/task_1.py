money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
num_of_months = 0  # Количество месяцев, которое можно протянуть без долгов

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while True:
    difference = spend - salary  # Недостаток средств
    if money_capital < difference:
        break

    spend *= 1 + increase
    money_capital -= difference
    num_of_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", num_of_months)
