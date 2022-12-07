import unittest
from src.loader import load, loads

json_from_load_ = {}


class TestLoad(unittest.TestCase):
    def test_load(self):
        global json_from_load_
        with open("tests/sample.json") as f:
            json_from_load = load(f)

        self.assertIsInstance(json_from_load, dict)
        json_from_load_ = json_from_load

    def test_loads(self):
        with open("tests/sample.json") as f:
            json_from_loads = loads(f.read())

        self.assertIsInstance(json_from_loads, dict)
        self.assertDictEqual(json_from_loads, json_from_load_)
