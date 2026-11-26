numbers = [int(part) for part in input("Целые числа через пробел: ").split()]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
