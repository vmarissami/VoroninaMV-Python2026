# Вариант 8. Числа от 10 до 20 включительно.
numbers = [int(part) for part in input("Целые числа через пробел: ").split()]
selected = []

for number in numbers:
    if 10 <= number <= 20:
        selected.append(number)

sorted_selected = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_selected}")
