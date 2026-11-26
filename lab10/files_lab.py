import csv


def read_matrix(path):
    with open(path, "r", encoding="utf-8") as source:
        header = source.readline()
        if not header:
            raise ValueError("Строка 1: файл пуст")

        try:
            rows, columns = map(int, header.split())
        except ValueError as error:
            raise ValueError("Строка 1: ожидаются два целых числа") from error
        if rows <= 0 or columns <= 0:
            raise ValueError("Строка 1: размеры должны быть больше нуля")

        matrix = []
        for line_number in range(2, rows + 2):
            line = source.readline()
            if not line:
                raise ValueError(f"Строка {line_number}: отсутствует строка данных")
            cells = line.split()
            if len(cells) != columns:
                raise ValueError(f"Строка {line_number}: ожидалось чисел — {columns}")
            try:
                matrix.append([int(cell) for cell in cells])
            except ValueError as error:
                raise ValueError(f"Строка {line_number}: все ячейки должны быть целыми числами") from error

        if source.readline():
            raise ValueError(f"Строка {rows + 2}: лишняя строка после данных")

    return matrix


def selected_sum(matrix):
    """Вернуть сумму элементов первой строки для варианта 8."""
    return sum(matrix[0]) if matrix else 0


def export_csv(matrix, path):
    with open(path, "w", encoding="utf-8", newline="") as target:
        csv.writer(target).writerows(matrix)
