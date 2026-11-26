def validate_records(records):
    """Проверить набор без изменений. При ошибке вызвать ValueError."""
    if not isinstance(records, list):
        raise ValueError("Ожидается список записей")

    seen_ids = set()
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Запись {index}: ожидается объект")
        record_id = record.get("id")
        if type(record_id) is not int or record_id <= 0:
            raise ValueError(f"Запись {index}: id должен быть положительным целым")
        if record_id in seen_ids:
            raise ValueError(f"Запись {index}: повторный ID {record_id}")
        seen_ids.add(record_id)

        for field in ("title", "category"):
            value = record.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Запись {index}: {field} должен быть непустой строкой")

        amount = record.get("amount")
        if type(amount) is not int or amount < 0:
            raise ValueError(f"Запись {index}: amount должен быть неотрицательным целым")
        if type(record.get("completed")) is not bool:
            raise ValueError(f"Запись {index}: completed должен быть логическим значением")


def add_record(records, title, category, amount):
    """Добавить запись в список и вернуть её. При неверных полях вызвать ValueError."""
    record_id = max((record["id"] for record in records), default=0) + 1
    record = {
        "id": record_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    validate_records([record])
    records.append(record)
    return record


def find_records(records, query):
    """Вернуть совпадения в исходном порядке, не меняя записи."""
    query = query.strip().casefold()
    if not query:
        raise ValueError("Введите непустую подстроку")
    return [record for record in records if query in record["title"].casefold()]


def get_record(records, record_id):
    """Вернуть запись по ID или None."""
    return next((record for record in records if record["id"] == record_id), None)


def set_completed(records, record_id, completed):
    """Установить статус и вернуть True. Для неизвестного ID вернуть False."""
    record = get_record(records, record_id)
    if record is None:
        return False
    if type(completed) is not bool:
        raise ValueError("Статус должен быть логическим значением")
    record["completed"] = completed
    return True


def delete_record(records, record_id):
    """Удалить запись из списка и вернуть True, если ID найден."""
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    """Вернуть количества, общий километраж и суммы по категориям без изменений входа."""
    completed = sum(record["completed"] for record in records)
    by_category = {}
    for record in records:
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]
    return {
        "total": len(records),
        "completed": completed,
        "pending": len(records) - completed,
        "amount": sum(by_category.values()),
        "by_category": dict(sorted(by_category.items())),
    }
