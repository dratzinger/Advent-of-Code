import unittest

from day6 import sum_answers, sum_answers_common
from util.parser import get_input_grouped


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(11, sum_answers(get_input_grouped("test_input.txt")))

    def test_part_2_known_input(self):
        self.assertEqual(6, sum_answers_common(get_input_grouped("test_input.txt")))


if __name__ == '__main__':
    unittest.main()
