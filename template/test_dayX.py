import unittest

from dayX import part_one, part_two

INPUT_0 = ""


class Test(unittest.TestCase):
    def test_part_1_known_input_1(self):
        self.assertEqual(0, part_one(INPUT_0))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(INPUT_0))


if __name__ == '__main__':
    unittest.main()
