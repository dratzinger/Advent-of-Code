# --- Day 10: Adapter Array ---
from typing import List

from util.parser import get_input_lines


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


# --- Part One ---
def differences_multiplied(data):
    dist = calculate_difference_distribution(data)
    return dist[1] * dist[3]


# --- Part Two ---
def part_two(data):
    count = 0
    return count


def main():
    data = get_input_lines()
    print(differences_multiplied(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
