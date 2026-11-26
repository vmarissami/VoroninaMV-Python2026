from contextlib import redirect_stdout
from io import StringIO

from collections_lab import (
    all_topics,
    common_topics,
    print_word_counts,
    ranked_totals,
    titles_in_category,
    totals_by_category,
    word_counts,
)

assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts("А:Б!\tа:б, : !") == {"а:б": 2}

output = StringIO()
with redirect_stdout(output):
    print_word_counts({"sql": 1, "python": 2})
assert output.getvalue() == "python: 2\nsql: 1\n"

first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]
assert common_topics([], first) == []
assert all_topics([], first) == ["python", "sql"]
assert common_topics(["SQL"], ["sql"]) == []

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
original = [record.copy() for record in records]
assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []
assert ranked_totals(records) == [("основное", 7), ("дополнительное", 2)]
assert records == original

tied_records = [
    {"title": "R1", "category": "водный", "amount": 4},
    {"title": "R2", "category": "пеший", "amount": 0},
    {"title": "R3", "category": "велосипедный", "amount": 4},
]
assert totals_by_category(tied_records) == {"водный": 4, "пеший": 0, "велосипедный": 4}
assert ranked_totals(tied_records) == [("велосипедный", 4), ("водный", 4), ("пеший", 0)]
assert ranked_totals([]) == []

print("Все 20 проверок пройдены")
