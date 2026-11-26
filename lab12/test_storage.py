import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from storage import load_records, save_records


class StorageTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = Path(directory.name) / "data.json"

    def test_round_trip(self):
        records = [
            {"id": 2, "title": "Сплав", "category": "водный", "amount": 4,
             "completed": True, "notes": None},
        ]
        save_records(self.path, records)
        self.assertEqual(load_records(self.path), records)
        self.assertIn("Сплав", self.path.read_text(encoding="utf-8"))

    def test_missing_and_invalid(self):
        with self.assertRaises(FileNotFoundError):
            load_records(self.path)
        for contents, expected in [
            (b"[", json.JSONDecodeError), (b"\xff", UnicodeError), (b"{}", ValueError),
        ]:
            self.path.write_bytes(contents)
            with self.subTest(contents=contents), self.assertRaises(expected):
                load_records(self.path)
            self.assertEqual(self.path.read_bytes(), contents)

    def test_failed_replace_preserves_previous_file(self):
        save_records(self.path, [])
        previous = self.path.read_bytes()
        with patch("storage.Path.replace", side_effect=PermissionError("Нет доступа")):
            with self.assertRaises(PermissionError):
                save_records(self.path, [])
        self.assertEqual(self.path.read_bytes(), previous)
        self.assertEqual(list(self.path.parent.iterdir()), [self.path])


if __name__ == "__main__":
    unittest.main()
