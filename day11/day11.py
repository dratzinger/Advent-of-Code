# --- Day 11: Seating System ---
import copy
from enum import Enum
from typing import Tuple

from util.parser import get_input_lines


class State:
    # seat states
    empty = 'L'
    occupied = '#'
    floor = '.'


class Layout:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[State.floor for _ in range(cols)] for _ in range(rows)]

    def __eq__(self, other) -> bool:
        return self.data == other.data

    def set_position(self, x: int, y: int, state: str):
        self.data[y][x] = state

    def seat_occupied(self, x: int, y: int):
        return self.data[y][x] == State.occupied

    def seat_empty(self, x: int, y: int):
        return self.data[y][x] == State.empty

    def count_occupied(self) -> int:
        return len([item for sublist in self.data for item in sublist if item == State.occupied])

    def apply_rules(self):
        sit_threshold = 0
        leave_threshold = 4

        for y in range(self.rows):
            for x in range(self.cols):
                if self.seat_empty(x, y):
                    if self.check_neighbours(x, y, State.occupied, sit_threshold):
                        # todo: fix this check
                        self.set_position(x, y, State.occupied)
                elif self.seat_occupied(x, y):
                    if self.check_neighbours(x, y, State.occupied, leave_threshold):
                        self.set_position(x, y, State.empty)
        return self

    def check_neighbours(self, x: int, y: int, state: str, threshold: int):
        for ny in [y-1, y, y+1]:
            for nx in [x-1, x, x+1]:
                if (threshold >= 0) and (0 <= nx < self.cols and 0 <= ny < self.rows) and (nx != x and ny != y):
                    threshold = threshold - (self.data[ny][nx] == state)
        return threshold >= 0

# --- Part One ---
def part_one(data):
    plan = build_seat_plan(data)
    count = simulate_seating(plan)
    return count


def build_seat_plan(data):
    rows = len(data)
    cols = len(data[0])
    plan = Layout(rows, cols)

    for row in range(rows):
        for seat in range(cols):
            plan.set_position(row, seat, data[row][seat])

    return plan


def simulate_seating(plan: Layout):
    previous = []
    while plan is not previous:
        previous = plan
        plan = seating_round(plan)

    return plan.count_occupied()


def seating_round(plan: Layout):
    result = copy.deepcopy(plan)
    result.apply_rules()
    return result


# --- Part Two ---
def part_two(data):
    count = 0
    return count


def main():
    data = get_input_lines()
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
