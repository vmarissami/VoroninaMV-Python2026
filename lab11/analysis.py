def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком задач")

    seen_ids = set()
    for index, task in enumerate(data, start=1):
        if not isinstance(task, dict):
            raise ValueError(f"Запись {index}: ожидается объект")

        for field in ("id", "userId"):
            value = task.get(field)
            if type(value) is not int or value <= 0:
                raise ValueError(f"Запись {index}: {field} должен быть положительным целым числом")

        title = task.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Запись {index}: title должен быть непустой строкой")
        if type(task.get("completed")) is not bool:
            raise ValueError(f"Запись {index}: completed должен быть логическим значением")

        task_id = task["id"]
        if task_id in seen_ids:
            raise ValueError(f"Запись {index}: повторный id {task_id}")
        seen_ids.add(task_id)


def completion_counts(todos):
    counts = {}
    for task in todos:
        user_id = task["userId"]
        counts.setdefault(user_id, 0)
        if task["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    maximum = max(counts.values(), default=0)
    if maximum == 0:
        return []
    return sorted(user_id for user_id, count in counts.items() if count == maximum)


def completed_leader_tasks(todos, leaders):
    leader_ids = set(leaders)
    return [task for task in todos if task["userId"] in leader_ids and task["completed"]]


def select_tasks(todos, user_id, parameter=None):
    """Вернуть задачи пользователя с указанной подстрокой в названии."""
    if parameter is None or not parameter.strip():
        raise ValueError("Подстрока должна быть непустой")
    substring = parameter.strip().casefold()
    return [
        task for task in todos
        if task["userId"] == user_id and substring in task["title"].casefold()
    ]
