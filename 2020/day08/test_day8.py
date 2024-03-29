import unittest
from util.parser import get_input_lines
from day8 import check_loop_acc_state, check_final_acc_state


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(5, check_loop_acc_state(get_input_lines("test_input.txt")))

    def test_part_2_known_input(self):
        self.assertEqual(8, check_final_acc_state(get_input_lines("test_input.txt")))


if __name__ == '__main__':
    unittest.main()
