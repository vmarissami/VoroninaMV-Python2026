import json
from pathlib import Path

from logic import add_record, delete_record, find_records, get_record, set_completed, statistics
from storage import load_records, save_records

DATA_PATH = Path(__file__).resolve().with_name("data.json")
MENU = """
1. Показать маршруты
2. Добавить маршрут
3. Найти маршруты
4. Изменить статус
5. Удалить маршрут
6. Показать статистику
7. Сохранить данные
8. Выйти"""


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Введите непустой текст")


def read_integer(prompt, minimum):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Введите целое число")
            continue
        if value >= minimum:
            return value
        print(f"Число должно быть не меньше {minimum}")


def read_yes_no(prompt):
    while True:
        answer = input(prompt).strip().casefold()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Введите «да» или «нет»")


def format_record(record):
    status = "пройден" if record["completed"] else "не пройден"
    return f'{record["id"]} | {record["title"]} | {record["category"]} | {record["amount"]} км | {status}'


def show_records(records, empty_message="Нет записей"):
    if not records:
        print(empty_message)
    for record in sorted(records, key=lambda item: item["id"]):
        print(format_record(record))


def add_route(records):
    title = read_text("Название: ")
    category = read_text("Категория: ")
    amount = read_integer("Длина в целых километрах: ", 0)
    record = add_record(records, title, category, amount)
    print(f'Маршрут добавлен. ID: {record["id"]}')


def change_status(records):
    record_id = read_integer("ID маршрута: ", 1)
    if get_record(records, record_id) is None:
        print("Маршрут с таким ID не найден")
        return
    completed = read_yes_no("Маршрут пройден? (да/нет): ")
    set_completed(records, record_id, completed)
    print("Статус обновлён")


def remove_route(records):
    record_id = read_integer("ID маршрута: ", 1)
    if get_record(records, record_id) is None:
        print("Маршрут с таким ID не найден")
        return
    if input("Удалить маршрут? (да/нет): ").strip().casefold() == "да":
        delete_record(records, record_id)
        print("Маршрут удалён")
    else:
        print("Удаление отменено")


def show_statistics(records):
    summary = statistics(records)
    print(f'Всего маршрутов: {summary["total"]}')
    print(f'Пройдено: {summary["completed"]}')
    print(f'Не пройдено: {summary["pending"]}')
    print(f'Общая длина: {summary["amount"]} км')
    print("Длина по категориям:")
    for category, amount in summary["by_category"].items():
        print(f"{category}: {amount} км")


def try_save(records, path):
    try:
        save_records(path, records)
    except (OSError, ValueError) as error:
        print(f"Ошибка сохранения: {error}")
        return False
    print("Данные сохранены")
    return True


def main(path=DATA_PATH):
    try:
        records = load_records(path)
    except FileNotFoundError:
        print("Файл data.json не найден. Создан пустой список маршрутов")
        records = []
    except UnicodeError:
        print("Ошибка кодировки: ожидается UTF-8")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: строка {error.lineno}, столбец {error.colno}")
        return
    except ValueError as error:
        print(f"Ошибка структуры: {error}")
        return
    except OSError as error:
        print(f"Ошибка чтения: {error}")
        return

    print("План туристических маршрутов")
    while True:
        print(MENU)
        command = input("Команда: ").strip()
        if command == "1":
            show_records(records)
        elif command == "2":
            add_route(records)
        elif command == "3":
            query = read_text("Подстрока названия: ")
            show_records(find_records(records, query), "Маршруты не найдены")
        elif command == "4":
            change_status(records)
        elif command == "5":
            remove_route(records)
        elif command == "6":
            show_statistics(records)
        elif command == "7":
            try_save(records, path)
        elif command == "8":
            if not read_yes_no("Сохранить перед выходом? (да/нет): ") or try_save(records, path):
                return
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
