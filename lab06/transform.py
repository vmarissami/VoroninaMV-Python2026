numbers = [int(part) for part in input("Целые числа через пробел: ").split()]
transformed = []

for number in numbers:
    transformed.append(abs(number))

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
