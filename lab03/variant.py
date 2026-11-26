# Вариант 8. Заполнение группы.
occupancy = int(input("Заполнение группы, %: "))

if occupancy < 0 or occupancy > 100:
    print("Ошибка диапазона")
elif occupancy < 40:
    print("Есть места")
elif occupancy < 80:
    print("Группа набирается")
else:
    print("Почти заполнена")
