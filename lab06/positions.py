numbers = [int(part) for part in input("Целые числа через пробел: ").split()]

if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)

    print(positions)
