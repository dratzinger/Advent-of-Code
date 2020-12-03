from unittest import TestCase

from day3 import count_trees

KNOWN_INPUT = []


class Test(TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(count_trees(KNOWN_INPUT), 0)
