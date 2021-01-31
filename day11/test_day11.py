import unittest
from day11 import part_one, build_seat_plan, seating_round
from test_input import *

class Test(unittest.TestCase):
    input = build_seat_plan(input_seats)
    target_1 = build_seat_plan(out_round_1)
    target_2 = build_seat_plan(out_round_2)
    target_3 = build_seat_plan(out_round_3)
    target_4 = build_seat_plan(out_round_4)

    # def test_part_1_known_input(self):
    #     self.assertEqual(37, part_one(input_seats))

    def test_part_1_round1(self):
        simulation = seating_round(build_seat_plan(input_seats))
        target_1 = build_seat_plan(out_round_1)
        self.assertTrue(simulation == target_1)


if __name__ == '__main__':
    unittest.main()
