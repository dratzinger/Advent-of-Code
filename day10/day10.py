# --- Day 10: Adapter Array ---
from typing import List

from util.parser import get_input_lines


# --- Part One ---
def calculate_difference_distribution(data: List[str]):
    distribution = [0, 0, 0, 1]  # built-in adapter is always 3 higher than the highest adapter
    joltages = sorted([int(i) for i in data])
    previous: int = 0
    for joltage in joltages:
        difference = joltage - previous
        if difference > 3:
            raise RuntimeWarning("Differences exceed specification")
        else:
            distribution[difference] += 1
        previous = joltage
    return distribution


def differences_multiplied(data):
    dist = calculate_difference_distribution(data)
    return dist[1] * dist[3]


# --- Part Two ---
def calculate_possible_arrangements(data: List[str]):
    numbers = sorted([int(i) for i in data])
    shift1 = shift_list(numbers)
    shift2 = shift_list(shift1)
    shift3 = shift_list(shift2)
    possible = [evaluate_options(i, j, k, l) for i, j, k, l in zip (numbers, shift1, shift2, shift3)]
    return prod(possible)

def prod(iterable):
    from functools import reduce
    import operator
    return reduce(operator.mul, iterable, 1)

def shift_list(l: list) -> list:
    from collections import deque
    q = deque(l)
    q.rotate(-1)
    return list(q)

def evaluate_options(i, j, k, l):
    count = 0
    count += (j - i <= 3)
    count += (k - i <= 3)
    count += (l - i <= 3)
    return count

def part_two(data):
    return calculate_possible_arrangements(data)


def main():
    data = get_input_lines()
    print(differences_multiplied(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
