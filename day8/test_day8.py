import unittest
from util.parser import get_input_lines
from day8 import part_one, part_two


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(5, part_one(get_input_lines("test_input.txt")))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(get_input_lines("test_input.txt")))


if __name__ == '__main__':
    unittest.main()
