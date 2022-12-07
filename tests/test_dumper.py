import json
import unittest

from src.dumper import dump, dumps


class TestDump(unittest.TestCase):
    def test_dump(self):
        with open("tests/dump.json", "w") as f:
            dump({"a": "bcd // Testing"}, f)

    def test_dumps(self):
        with open("tests/dumps.json", "w") as f:
            dumps("{'a': \"bcd // Testing\"} // Testing", f)

    def test_equiv(self):
        with open("tests/dump.json") as dump_file:
            with open("tests/dumps.json") as dumps_file:
                dumps_object = json.load(dumps_file)
            dump_object = json.load(dump_file)
        self.assertDictEqual(dump_object, dumps_object)
