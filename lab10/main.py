from pathlib import Path

from files_lab import export_csv, read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer():
    while True:
        try:
            number = int(input("Введите положительный целый размер: "))
        except ValueError:
            print("Ошибка: не целое число")
            continue

        if number > 0:
            return number
        print("Ошибка: должно быть больше нуля")


def main():
    size = read_positive_integer()
    print(f"Принят размер: {size}")

    folder = Path(__file__).resolve().parent
    try:
        matrix = read_matrix(folder / "matrix.txt")
    except FileNotFoundError:
        print("Входной файл matrix.txt не найден")
        return
    except UnicodeError:
        print("Ошибка кодировки: matrix.txt должен быть в UTF-8")
        return
    except ValueError as error:
        print(f"Ошибка формата: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа при чтении matrix.txt: {error}")
        return

    rows = " ".join(map(str, row_sums(matrix)))
    columns = " ".join(map(str, column_sums(matrix)))
    report = f"Суммы строк: {rows}\nСуммы столбцов: {columns}\nРезультат варианта: {selected_sum(matrix)}\n"

    try:
        (folder / "report.txt").write_text(report, encoding="utf-8")
    except OSError as error:
        print(f"Ошибка записи report.txt: {error}")
        return
    print("Отчёт сохранён в report.txt")

    try:
        export_csv(matrix, folder / "matrix.csv")
    except OSError as error:
        print(f"Ошибка записи matrix.csv: {error}")
    else:
        print("Матрица экспортирована в matrix.csv")


if __name__ == "__main__":
    main()
