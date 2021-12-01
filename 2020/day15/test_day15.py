import unittest

from day15 import part_one, part_two


class Test(unittest.TestCase):
    def test_part_1_known_input_1(self):
        self.assertEqual(436, part_one([0, 3, 6]))

    def test_part_1_known_input_2(self):
        self.assertEqual(1, part_one([1, 3, 2]))

    def test_part_1_known_input_3(self):
        self.assertEqual(10, part_one([2, 1, 3]))

    def test_part_1_known_input_4(self):
        self.assertEqual(27, part_one([1, 2, 3]))

    def test_part_1_known_input_5(self):
        self.assertEqual(78, part_one([2, 3, 1]))

    def test_part_1_known_input_7(self):
        self.assertEqual(438, part_one([3, 2, 1]))

    def test_part_1_known_input_8(self):
        self.assertEqual(1836, part_one([3, 1, 2]))

    def test_part_2_known_input(self):
        self.assertEqual(175594, part_two([0, 3, 6]))


if __name__ == '__main__':
    unittest.main()
