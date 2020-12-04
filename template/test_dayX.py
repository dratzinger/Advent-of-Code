from unittest import TestCase

from dayX import part_one, part_two

KNOWN_INPUT = []


class Test(TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(part_one(KNOWN_INPUT), 0)

    def test_part_2_known_input(self):
        self.assertEqual(part_two(KNOWN_INPUT), 0)
