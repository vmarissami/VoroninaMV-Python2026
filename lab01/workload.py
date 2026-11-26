first_subject = input("Первый предмет: ")
first_lessons = int(input("Количество занятий по первому предмету: "))
first_duration = int(input("Длительность занятия по первому предмету, мин: "))

second_subject = input("Второй предмет: ")
second_lessons = int(input("Количество занятий по второму предмету: "))
second_duration = int(input("Длительность занятия по второму предмету, мин: "))

available_hours = float(input("Доступное время на неделю, ч: "))

first_minutes = first_lessons * first_duration
second_minutes = second_lessons * second_duration
total_minutes = first_minutes + second_minutes
total_hours = total_minutes / 60
free_hours = available_hours - total_hours

print("\nУчебная нагрузка")
print(f"{first_subject}: {first_minutes} мин")
print(f"{second_subject}: {second_minutes} мин")
print(f"Нагрузка за неделю: {total_minutes} мин ({total_hours:.2f} ч)")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {total_hours * 4:.2f} ч")
