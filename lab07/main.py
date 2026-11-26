from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input("Целое число: "))
    numbers = [int(part) for part in input("Целые числа через пробел: ").split()]
    text = input("Произвольный текст: ")
    threshold = int(input("Неотрицательный целый порог: "))

    print(f"Сумма цифр: {sum_digits(number)}")
    mean = average(numbers)
    if mean is None:
        print("Нет данных")
    else:
        print(f"Среднее: {mean}")

    print(f"Нормализованный текст: {normalize_text(text)}")
    print(f"Выборка: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()
