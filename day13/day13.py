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
    schedule = (data[1].split(","))
    buses = [(int(bus), offset) for offset, bus in enumerate(schedule) if bus != 'x']
    ranges = [
        (bus, buses[i+1][1]-offset) if (i+1 < len(buses)) else (bus, 1)
        for i, (bus, offset) in enumerate(buses)
    ]
    # ranges.reverse()
    first, _ = buses.pop(0)
    # checks = sorted((bus for bus in ranges), reverse=True)
    # checks.append(first)
    fltr = (x*first for x in infinite_int())
    for freq, diff in buses:
        fltr = (x for x in fltr if x % freq == 0 and x % first == diff)
        if freq == 59:
            for _ in range(1000):
                print(next(fltr))
    return next(fltr)


def infinite_int():
    i = 0
    while True:
        yield i
        i += 1


def main():
    data = get_input_lines()
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
