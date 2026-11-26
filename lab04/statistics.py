n = int(input("Количество чисел: "))
first_number = int(input("Число 1: "))

total = first_number
maximum = first_number
positive_count = 0
if first_number > 0:
    positive_count = 1

for index in range(2, n + 1):
    number = int(input(f"Число {index}: "))
    total += number
    if number > 0:
        positive_count += 1
    if number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных чисел: {positive_count}")
print(f"Максимум: {maximum}")
