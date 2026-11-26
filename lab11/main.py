import json
from pathlib import Path

from analysis import (
    completed_leader_tasks,
    completion_counts,
    select_tasks,
    top_users,
    validate_todos,
)


def read_user_id():
    while True:
        try:
            user_id = int(input("ID пользователя: "))
        except ValueError:
            print("Введите целое число")
            continue
        if user_id > 0:
            return user_id
        print("ID должен быть больше нуля")


def read_substring():
    while True:
        substring = input("Подстрока в названии: ").strip()
        if substring:
            return substring
        print("Подстрока не должна быть пустой")


def save_json(path, data):
    with path.open("w", encoding="utf-8") as target:
        json.dump(data, target, ensure_ascii=False, indent=2)
        target.write("\n")


def main():
    folder = Path(__file__).resolve().parent
    try:
        with (folder / "todos.json").open(encoding="utf-8") as source:
            todos = json.load(source)
        validate_todos(todos)
    except FileNotFoundError:
        print("Файл todos.json не найден")
        return
    except UnicodeError:
        print("Файл todos.json должен быть в UTF-8")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: строка {error.lineno}, столбец {error.colno}")
        return
    except ValueError as error:
        print(f"Ошибка структуры: {error}")
        return
    except OSError as error:
        print(f"Ошибка чтения todos.json: {error}")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)
    leader_tasks = completed_leader_tasks(todos, leaders)
    selected = select_tasks(todos, read_user_id(), read_substring())

    print(f"Количество завершённых задач: {dict(sorted(counts.items()))}")
    print(f"Лидеры: {leaders}")
    print(f"ID завершённых задач лидеров: {[task['id'] for task in leader_tasks]}")
    print(f"ID выбранных задач: {[task['id'] for task in selected]}")

    try:
        save_json(folder / "leaders.json", leader_tasks)
        save_json(folder / "selected.json", selected)
    except (OSError, UnicodeError) as error:
        print(f"Ошибка сохранения: {error}")
    else:
        print("Результаты сохранены в leaders.json и selected.json")


if __name__ == "__main__":
    main()
