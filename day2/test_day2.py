import unittest

from day2 import count_valid_passwords, count_valid_passwords_pos

KNOWN_INPUT = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"]


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(2, count_valid_passwords(KNOWN_INPUT))

    def test_part_2_known_input(self):
        self.assertEqual(1, count_valid_passwords_pos(KNOWN_INPUT))


if __name__ == '__main__':
    unittest.main()
