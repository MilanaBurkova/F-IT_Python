users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статистикой посещений

statistic_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

statistic_["Общее количество"] = len(users)
statistic_["Уникальные посещения"] = len(set(users))

print(statistic_)
