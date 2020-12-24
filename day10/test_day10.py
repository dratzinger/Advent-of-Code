import unittest
from util.parser import get_input_lines
from day10 import differences_multiplied, part_two


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(22 * 10, differences_multiplied(get_input_lines("test_input.txt")))

    def test_part_2_known_input(self):
        self.assertEqual(19208, part_two(get_input_lines("test_input.txt")))


if __name__ == '__main__':
    unittest.main()
