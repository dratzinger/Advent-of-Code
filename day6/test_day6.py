import unittest

from day6 import part_one, part_two

KNOWN_INPUT = ["abc",
                "",
                "a",
                "b",
                "c",
                "",
                "ab",
                "ac",
                "",
                "a",
                "a",
                "a",
                "a",
                "",
                "b"]


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(11, part_one(KNOWN_INPUT))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(KNOWN_INPUT))


if __name__ == '__main__':
    unittest.main()
