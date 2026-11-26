def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


def factorial_iterative(number):
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


if __name__ == "__main__":
    for number in range(21):
        recursive = factorial(number)
        iterative = factorial_iterative(number)
        assert recursive == iterative
        print(f"{number}! = {recursive}")
    print("Результаты совпадают для чисел от 0 до 20")
