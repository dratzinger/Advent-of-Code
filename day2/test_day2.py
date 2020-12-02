from unittest import TestCase

from day2 import count_valid_passwords, count_valid_passwords_pos

KNOWN_INPUT = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"]


class Test(TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(count_valid_passwords(KNOWN_INPUT), 2)

    def test_part_2_known_input(self):
        self.assertEqual(count_valid_passwords_pos(KNOWN_INPUT), 1)
