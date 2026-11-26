# Вариант 8. Числа с модулем больше 5.
n = int(input("Количество чисел: "))
selected_count = 0
selected_sum = 0

for index in range(1, n + 1):
    number = int(input(f"Число {index}: "))
    if abs(number) > 5:
        selected_count += 1
        selected_sum += number

print(f"Количество: {selected_count}")
print(f"Сумма: {selected_sum}")
