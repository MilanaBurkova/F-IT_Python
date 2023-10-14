salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Подушка безопасности

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

for num in range(months):
    difference = spend - salary  # Недостаток средств
    spend *= 1 + increase
    money_capital += difference

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
