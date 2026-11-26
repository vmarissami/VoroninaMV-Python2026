numbers = [int(part) for part in input("Целые числа через пробел: ").split()]

if not numbers:
    print("Нет данных")
else:
    count = len(numbers)
    total = sum(numbers)
    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {total / count:.2f}")
