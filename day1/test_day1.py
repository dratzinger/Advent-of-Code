import unittest

from day1 import brute_force, brute_force_three


class Test(unittest.TestCase):
    def test_part_1_known_numbers(self):
        known = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(514579, brute_force(known))

    def test_part_1_no_correct_numbers(self):
        known = [1721, 979, 36, 29, 675, 1456]
        self.assertNotEqual(514579, brute_force_three(known))

    def test_part_2_known_numbers(self):
        known = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(241861950, brute_force_three(known))

    def test_part_2_no_correct_numbers(self):
        known = [1721, 979, 36, 299, 675, 1456]
        self.assertNotEqual(241861950, brute_force_three(known))


if __name__ == '__main__':
    unittest.main()
