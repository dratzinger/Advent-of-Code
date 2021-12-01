import unittest

from day3 import count_trees, check_slopes

MOVE_RIGHT = 3
MOVE_DOWN = 1
KNOWN_INPUT = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"]

SLOPES = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(7, count_trees(KNOWN_INPUT, MOVE_RIGHT, MOVE_DOWN))

    def test_part_2_known_input(self):
        self.assertEqual(336, check_slopes(KNOWN_INPUT, SLOPES))


if __name__ == '__main__':
    unittest.main()
