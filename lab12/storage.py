import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from logic import validate_records


def load_records(path):
    """Прочитать и проверить список записей, передавая ошибки вызывающему коду."""
    with Path(path).open(encoding="utf-8") as source:
        records = json.load(source)
    validate_records(records)
    return records


def save_records(path, records):
    """Проверить записи и заменить JSON после успешной записи временного файла."""
    validate_records(records)
    path = Path(path)
    temporary_path = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False,
        ) as target:
            temporary_path = Path(target.name)
            json.dump(records, target, ensure_ascii=False, indent=2)
            target.write("\n")
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
