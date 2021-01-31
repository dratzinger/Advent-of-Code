import unittest
from util.parser import get_input_lines
from day11 import part_one, part_two
from test_input import *

class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(37, part_one(input_seats))


if __name__ == '__main__':
    unittest.main()
