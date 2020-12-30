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
def evaluate_possible(data: List[int]):
    count = 0
    for end in branches(data, 0, len(data) - 1):
        count += end
    return count

def branches(data: List[int], pointer: int, target: int):
    for offset in [1,2,3]:
        if (pointer + offset) < target:
            if adapter_suitable(data, pointer, offset):
                branches(data, pointer + offset, target)
        else:
            yield 1

def adapter_suitable(data: List[int], pointer: int, offset: int):
        return data[pointer + offset] - data[pointer] <= 3

def part_two(data):
    numbers = sorted([int(i) for i in data])
    return evaluate_possible(numbers)


def main():
    data = get_input_lines()
    print(differences_multiplied(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
