from unittest import TestCase

from day3 import count_trees

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


class Test(TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(count_trees(KNOWN_INPUT, MOVE_RIGHT, MOVE_DOWN), 7)
