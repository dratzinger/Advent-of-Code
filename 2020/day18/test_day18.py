import unittest

from day18 import calculate, calculate_prioritized

EXPRESSION_0 = "1 + (2 * 3) + (4 * (5 + 6))"
EXPRESSION_1 = "2 * 3 + (4 * 5)"
EXPRESSION_2 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
EXPRESSION_3 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
EXPRESSION_4 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


class Test(unittest.TestCase):
    def test_part_1_known_input_1(self):
        self.assertEqual(26, calculate(EXPRESSION_1))

    def test_part_1_known_input_2(self):
        self.assertEqual(437, calculate(EXPRESSION_2))

    def test_part_1_known_input_3(self):
        self.assertEqual(12240, calculate(EXPRESSION_3))

    def test_part_1_known_input_4(self):
        self.assertEqual(13632, calculate(EXPRESSION_4))

    def test_part_2_known_input(self):
        self.assertEqual(51, calculate_prioritized(EXPRESSION_0))

    def test_part_2_known_input_1(self):
        self.assertEqual(46, calculate_prioritized(EXPRESSION_1))

    def test_part_2_known_input_2(self):
        self.assertEqual(1445, calculate_prioritized(EXPRESSION_2))

    def test_part_2_known_input_3(self):
        self.assertEqual(669060, calculate_prioritized(EXPRESSION_3))

    def test_part_2_known_input_4(self):
        self.assertEqual(23340, calculate_prioritized(EXPRESSION_4))


if __name__ == '__main__':
    unittest.main()
