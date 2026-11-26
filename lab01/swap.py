first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print("\nДо обмена")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")

temporary_room = first_room
first_room = second_room
second_room = temporary_room

print("\nПосле обмена")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")
