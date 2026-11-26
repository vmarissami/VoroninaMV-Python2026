number = int(input("Введите положительное целое число: "))
rejected_count = 0

while number <= 0:
    rejected_count += 1
    number = int(input("Введите положительное целое число: "))

print(f"Квадрат: {number ** 2}")
print(f"Отклонено попыток: {rejected_count}")
