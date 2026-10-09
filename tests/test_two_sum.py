import json
import unittest
from pathlib import Path

from taskee import two_sum

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "data" / "two_sum_cases.json").read_text(encoding="utf-8"))["cases"]


class TestTwoSum(unittest.TestCase):
    def test_dataset(self):
        self.assertGreaterEqual(len(CASES), 1, "at least one dataset is required")
        for case in CASES:
            with self.subTest(case["id"]):
                self.assertEqual(tuple(case["expected"]), two_sum(list(case["nums"]), case["target"]))

    def test_no_answer_raises(self):
        with self.assertRaises(ValueError):
            two_sum([1, 2], 100)


if __name__ == "__main__":
    unittest.main()
