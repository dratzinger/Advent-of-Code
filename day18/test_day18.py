import unittest

from day18 import calculate, part_two


class Test(unittest.TestCase):
    def test_part_1_known_input_1(self):
        self.assertEqual(26, calculate("2 * 3 + (4 * 5)"))

    def test_part_1_known_input_2(self):
        self.assertEqual(437, calculate("5 + (8 * 3 + 9 + 3 * 4 * 3)"))

    def test_part_1_known_input_3(self):
        self.assertEqual(12240, calculate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))

    def test_part_1_known_input_4(self):
        self.assertEqual(13632, calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two([]))


if __name__ == '__main__':
    unittest.main()
