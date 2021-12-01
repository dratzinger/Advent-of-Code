import unittest

from day22 import part_one, part_two
from util.parser import get_input_grouped

INPUT_0 = (get_input_grouped("test_input.txt", ":"))


class Test(unittest.TestCase):
    def test_part_1_known_input_1(self):
        self.assertEqual(306, part_one(INPUT_0))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(""))


if __name__ == '__main__':
    unittest.main()
