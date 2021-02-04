import unittest
from util.parser import get_input_lines
from day9 import part_one, part_two


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(127, part_one(get_input_lines("test_input.txt"), 5))

    def test_part_2_known_input(self):
        step_1 = part_one(get_input_lines("test_input.txt"), 5)
        self.assertEqual(62, part_two(get_input_lines("test_input.txt"), step_1))


if __name__ == '__main__':
    unittest.main()
