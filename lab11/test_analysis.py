import json
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (
    completed_leader_tasks,
    completion_counts,
    select_tasks,
    top_users,
    validate_todos,
)
from main import save_json


def ids(tasks):
    return [task["id"] for task in tasks]


def expect_invalid(data):
    try:
        validate_todos(data)
    except ValueError:
        return
    raise AssertionError(f"Некорректный набор принят: {data!r}")


def main():
    folder = Path(__file__).resolve().parent
    with (folder / "todos.json").open(encoding="utf-8") as source:
        todos = json.load(source)
    validate_todos(todos)
    original = [task.copy() for task in todos]

    counts = completion_counts(todos)
    assert counts == {5: 2, 10: 2}
    leaders = top_users(counts)
    assert leaders == [5, 10]
    leader_tasks = completed_leader_tasks(todos, leaders)
    assert ids(leader_tasks) == [1, 3, 4, 5]

    for dataset, expected in [([], {}), ([todos[1]], {5: 0})]:
        validate_todos(dataset)
        assert completion_counts(dataset) == expected
        assert top_users(expected) == []
        assert completed_leader_tasks(dataset, []) == []

    unique_leader = todos[:4]
    assert top_users(completion_counts(unique_leader)) == [10]
    assert ids(completed_leader_tasks(unique_leader, [10])) == [3, 4]
    assert top_users({10: 2, 5: 2, 2: 0}) == [5, 10]

    selected = select_tasks(todos, 5, "и")
    assert ids(selected) == [2, 5]
    assert ids(select_tasks(todos, 5, " СпИс ")) == [5]
    assert select_tasks(todos, 999, "и") == []
    assert select_tasks(todos, 5, "нет совпадений") == []
    assert todos == original

    no_user_id = todos[0].copy()
    del no_user_id["userId"]
    for dataset in [
        {},
        [todos[0], todos[0].copy()],
        [no_user_id],
        [dict(todos[0], completed="false")],
        [dict(todos[0], id=True)],
        [dict(todos[0], title=" ")],
        [dict(todos[0], userId=0)],
        [None],
    ]:
        expect_invalid(dataset)
    validate_todos([dict(todos[0], extra=None)])

    with TemporaryDirectory() as directory:
        temporary = Path(directory)
        for filename, expected in [("leaders.json", leader_tasks), ("selected.json", selected)]:
            path = temporary / filename
            save_json(path, expected)
            with path.open(encoding="utf-8") as source:
                assert json.load(source) == expected

        for filename in ("analysis.py", "main.py"):
            shutil.copyfile(folder / filename, temporary / filename)

        original_outputs = {
            filename: (temporary / filename).read_bytes()
            for filename in ("leaders.json", "selected.json")
        }
        input_path = temporary / "todos.json"
        for content, expected in [
            (None, "Файл todos.json не найден"),
            (b"\xff", "должен быть в UTF-8"),
            (b"[", "Ошибка JSON"),
            (b"{}", "Ошибка структуры"),
        ]:
            if content is not None:
                input_path.write_bytes(content)
            result = subprocess.check_output(
                [sys.executable, "-B", str(temporary / "main.py")],
                input="", text=True, timeout=5,
            )
            assert expected in result
            for filename, previous in original_outputs.items():
                assert (temporary / filename).read_bytes() == previous

    print("Все проверки пройдены")


if __name__ == "__main__":
    main()
