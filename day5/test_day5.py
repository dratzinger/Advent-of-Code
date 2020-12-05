import unittest

from day5 import find_highest_id, part_two, calculate_seat_id

KNOWN_INPUT = [
    ("BFFFBBFRRR", 70, 7, 567),
    ("FFFBBBFRRR", 14, 7, 119),
    ("BBFFBBFRLL", 102, 4, 820)
]


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        for tpl in KNOWN_INPUT:
            self.assertEqual(tpl[3], calculate_seat_id(tpl[0]))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(KNOWN_INPUT))


if __name__ == '__main__':
    unittest.main()
