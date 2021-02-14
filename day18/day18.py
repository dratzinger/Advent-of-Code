# --- Day 18: Operation Order ---
from typing import Iterable

from util.parser import get_input_lines


# --- Part One ---
def calculate(expression: str):
    return expression


def part_one(data: Iterable) -> int:
    expressions = (calculate(exp) for exp in data)
    return sum(expressions)


# --- Part Two ---
def part_two(data: Iterable) -> int:
    return 0


def main():
    data = (get_input_lines())
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
