# --- Day 13: Shuttle Search ---
from typing import List, Tuple
from math import floor, ceil
from util.parser import get_input_lines


# --- Part One ---
def closest_bus(timestamp: int, buses: List[int]) -> Tuple[int, int]:
    times = departure_window(timestamp, buses)
    wait = ((time-timestamp, bus) for time, bus in times if time >= timestamp)
    return min(wait)


def departure_window(timestamp: int, buses: List[int]):
    for bus in buses:
        factor = timestamp / bus
        yield floor(factor) * bus, bus
        yield ceil(factor) * bus, bus


def part_one(data):
    timestamp = int(data[0])
    buses = (data[1].split(","))
    in_service = [int(bus) for bus in buses if bus != 'x']
    bus, wait = closest_bus(timestamp, in_service)
    return bus * wait


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
