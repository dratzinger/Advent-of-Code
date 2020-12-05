# --- Day 5: Binary Boarding ---
import re

from typing import List

ROW_COUNT = 128
ROW_UPPER = "B"
COL_COUNT = 8
COL_UPPER = "R"


def prepare_string(line: str):
    return line.strip("\n")


def calculate_row(row_string: str) -> int:
    return recursive_find(list(row_string), list(range(0, ROW_COUNT)), ROW_UPPER)


def calculate_column(col_string: str) -> int:
    return recursive_find(list(col_string), list(range(0, COL_COUNT)), COL_UPPER)


def recursive_find(row_string, numbers, upper_char) -> int:
    direction = row_string.pop(0)
    middle_index = len(numbers)//2
    lower_half = numbers[:middle_index]
    upper_half = numbers[middle_index:]
    temp = upper_half if upper_char == direction else lower_half
    return temp.pop(0) if len(temp) == 1 else recursive_find(row_string, temp, upper_char)


def calculate_seat_id(pass_string: str):
    row_string = re.findall('^[BF]+', pass_string)[0]
    col_string = re.findall('[LR]+$', pass_string)[0]
    row = calculate_row(row_string)
    col = calculate_column(col_string)
    return row * 8 + col

# --- Part One ---
def find_highest_id(lines):
    ids = []
    for line in lines:
        line = prepare_string(line)
        ids.append(calculate_seat_id(line))
    return max(ids)


# --- Part Two ---
def part_two(lines):
    count = 0
    return count


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()

    print(find_highest_id(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()
