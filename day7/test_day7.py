import unittest
from util.parser import get_input_lines
from day7 import count_containing_rules, count_individual_bags


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(4, count_containing_rules(get_input_lines("test_input.txt")))

    def test_part_2_known_input(self):
        self.assertEqual(126, count_individual_bags(get_input_lines("test_input_2.txt")))


if __name__ == '__main__':
    unittest.main()
