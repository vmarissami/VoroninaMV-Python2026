import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import export_csv, read_matrix, selected_sum


def expect_format_error(path, contents, line_number):
    path.write_text(contents, encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError as error:
        assert f"Строка {line_number}:" in str(error)
    else:
        assert False, "Ошибка не обнаружена"


def main():
    with TemporaryDirectory() as directory:
        folder = Path(directory)
        path = folder / "matrix.txt"

        path.write_text("1 2\n7 -1\n", encoding="utf-8")
        assert read_matrix(path) == [[7, -1]]

        path.write_text("1 1\n0", encoding="utf-8")
        assert read_matrix(path) == [[0]]

        expect_format_error(path, "", 1)
        expect_format_error(path, "0 3\n", 1)
        expect_format_error(path, "1 x\n", 1)
        expect_format_error(path, "1 2\n1\n", 2)
        expect_format_error(path, "1 2\n1 x\n", 2)
        expect_format_error(path, "1 1\n1\n2\n", 3)
        expect_format_error(path, "1 1\n1\n\n", 3)
        expect_format_error(path, "2 1\n1\n", 3)
        expect_format_error(path, "1 1\n\n", 2)

        try:
            read_matrix(folder / "missing.txt")
        except FileNotFoundError:
            pass
        else:
            assert False, "Отсутствие файла не обнаружено"

        assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 2
        assert selected_sum([[7]]) == 7
        assert selected_sum([]) == 0

        csv_path = folder / "matrix.csv"
        export_csv([[1, -2], [0, 6]], csv_path)
        with open(csv_path, encoding="utf-8", newline="") as exported:
            assert list(csv.reader(exported)) == [["1", "-2"], ["0", "6"]]

    print("Все проверки пройдены")


if __name__ == "__main__":
    main()
