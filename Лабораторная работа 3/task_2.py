# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter=","):
    intersection_group = set(first_group.split(delimiter)).intersection(list(second_group.split(delimiter)))
    result = list(intersection_group)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
general_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(general_participants)
