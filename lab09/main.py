from table import column_sums, diagonal_pattern, row_sums, transform


def main():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    while rows <= 0 or columns <= 0:
        print("Размеры должны быть больше нуля")
        rows = int(input("Количество строк: "))
        columns = int(input("Количество столбцов: "))

    matrix = []
    for row_index in range(rows):
        row = [int(part) for part in input(f"Строка {row_index + 1}: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)

    print("Суммы строк:", *row_sums(matrix))
    print("Суммы столбцов:", *column_sums(matrix))

    size = int(input("Размер диагонального узора: "))
    while size <= 0:
        print("Размер должен быть больше нуля")
        size = int(input("Размер диагонального узора: "))

    print("Диагональный узор:")
    for row in diagonal_pattern(size):
        print(*row)

    print("Исходная таблица:")
    for row in matrix:
        print(*row)

    print("Преобразованная таблица:")
    for row in transform(matrix):
        print(*row)


if __name__ == "__main__":
    main()
