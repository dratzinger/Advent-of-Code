import unittest

from day5 import part_one, part_two

KNOWN_INPUT = []


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(0, part_one(KNOWN_INPUT))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(KNOWN_INPUT))


if __name__ == '__main__':
    unittest.main()
