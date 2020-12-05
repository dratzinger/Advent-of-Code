import unittest

from day5 import calculate_seat_id, calculate_row, calculate_column

KNOWN_INPUT = [
    ("BFFFBBFRRR", 70, 7, 567),
    ("FFFBBBFRRR", 14, 7, 119),
    ("BBFFBBFRLL", 102, 4, 820)
]


class Test(unittest.TestCase):
    def test_seat_id(self):
        for tpl in KNOWN_INPUT:
            self.assertEqual(tpl[3], calculate_seat_id(tpl[0]))

    def test_row(self):
        for tpl in KNOWN_INPUT:
            self.assertEqual(tpl[1], calculate_row(tpl[0]))

    def test_column(self):
        for tpl in KNOWN_INPUT:
            self.assertEqual(tpl[2], calculate_column(tpl[0]))


if __name__ == '__main__':
    unittest.main()
