import unittest
from copy import deepcopy

from logic import add_record, delete_record, find_records, set_completed, statistics, validate_records


class LogicTests(unittest.TestCase):
    def test_empty(self):
        validate_records([])
        self.assertEqual(find_records([], "тропа"), [])
        self.assertEqual(statistics([]), {
            "total": 0, "completed": 0, "pending": 0, "amount": 0, "by_category": {},
        })

    def test_add_and_delete(self):
        records = []
        first = add_record(records, "  Тропа  ", " пеший ", 4)
        second = add_record(records, "Тропа", "пеший", 2)
        self.assertEqual(first, {
            "id": 1, "title": "Тропа", "category": "пеший", "amount": 4, "completed": False,
        })
        self.assertEqual(second["id"], 2)
        self.assertTrue(delete_record(records, 1))
        self.assertEqual(records[0]["id"], 2)
        self.assertEqual(add_record(records, "Сплав", "водный", 0)["id"], 3)

    def test_search_and_status(self):
        records = []
        record = add_record(records, "Лесная тропа", "пеший", 4)
        original = deepcopy(records)
        self.assertEqual(find_records(records, " ТРОПА "), [record])
        self.assertEqual(find_records(records, "сплав"), [])
        with self.assertRaises(ValueError):
            find_records(records, " ")
        self.assertFalse(set_completed(records, 99, True))
        self.assertFalse(delete_record(records, 99))
        self.assertEqual(records, original)
        self.assertTrue(set_completed(records, 1, True))
        self.assertTrue(set_completed(records, 1, True))
        self.assertIs(record["completed"], True)
        self.assertTrue(set_completed(records, 1, False))
        self.assertIs(record["completed"], False)

    def test_statistics(self):
        records = []
        add_record(records, "Тропа", "пеший", 4)
        add_record(records, "Сплав", "водный", 2)
        set_completed(records, 2, True)
        original = deepcopy(records)
        summary = statistics(records)
        self.assertEqual(summary, {
            "total": 2, "completed": 1, "pending": 1, "amount": 6,
            "by_category": {"водный": 2, "пеший": 4},
        })
        self.assertEqual(list(summary["by_category"]), ["водный", "пеший"])
        self.assertEqual(records, original)

    def test_validation(self):
        valid = {"id": 1, "title": "Тропа", "category": "пеший", "amount": 4, "completed": False}
        validate_records([dict(valid, note=None)])
        for dataset in [
            {}, [None], [valid, valid.copy()],
            [dict(valid, id=True)], [dict(valid, id=0)], [dict(valid, title=" ")],
            [dict(valid, category=[])], [dict(valid, amount=True)],
            [dict(valid, amount=-1)], [dict(valid, amount=1.5)], [dict(valid, completed=0)],
        ]:
            with self.subTest(dataset=dataset), self.assertRaises(ValueError):
                validate_records(dataset)
        for field in valid:
            incomplete = valid.copy()
            del incomplete[field]
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_records([incomplete])


if __name__ == "__main__":
    unittest.main()
