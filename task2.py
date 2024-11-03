def find_common_participants(s1, s2, s3=','):
    list1 = s1.split(s3)
    list2 = s2.split(s3)
    list3 = list(set(list1).intersection(list2))
    list3.sort()
    return list3


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
