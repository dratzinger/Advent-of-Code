from unittest import TestCase

from day1 import brute_force, brute_force_three


class Test(TestCase):
    def test_part_1_known_numbers(self):
        known = [1721, 979, 366, 299, 675, 1456]
        self.assertEquals(brute_force(known), 514579)

    def test_part_1_no_correct_numbers(self):
        known = [1721, 979, 36, 29, 675, 1456]
        self.assertNotEquals(brute_force_three(known), 514579)

    def test_part_2_known_numbers(self):
        known = [1721, 979, 366, 299, 675, 1456]
        self.assertEquals(brute_force_three(known), 241861950)

    def test_part_2_no_correct_numbers(self):
        known = [1721, 979, 36, 299, 675, 1456]
        self.assertNotEquals(brute_force_three(known), 241861950)