# --- Day 5: Binary Boarding ---
import re

from typing import List

ROW_COUNT = 128
ROW_UPPER = "B"
COL_COUNT = 8
COL_UPPER = "R"
IDS = []


def prepare_string(line: str):
    return line.strip("\n")


def calculate_row(row_string: str) -> int:
    row_string = re.findall('^[BF]+', row_string)[0]
    return recursive_find(list(row_string), list(range(0, ROW_COUNT)), ROW_UPPER)


def calculate_column(col_string: str) -> int:
    col_string = re.findall('[LR]+$', col_string)[0]
    return recursive_find(list(col_string), list(range(0, COL_COUNT)), COL_UPPER)


def recursive_find(row_string, numbers, upper_char) -> int:
    direction = row_string.pop(0)
    middle_index = len(numbers)//2
    lower_half = numbers[:middle_index]
    upper_half = numbers[middle_index:]
    temp = upper_half if upper_char == direction else lower_half
    return temp.pop(0) if len(temp) == 1 else recursive_find(row_string, temp, upper_char)


def calculate_seat_id(pass_string: str):
    row = calculate_row(pass_string)
    col = calculate_column(pass_string)
    return row * 8 + col


def calculate_ids(lines):
    for line in lines:
        line = prepare_string(line)
        IDS.append(calculate_seat_id(line))


# --- Part One ---
def find_highest_id():
    return max(IDS)


# --- Part Two ---
def find_my_seat():
    seats = sorted(IDS)
    prev: int
    current = seats.pop(0)
    while len(seats) > 0:
        prev = current
        current = seats.pop(0)
        if prev+2 == current:
            return prev+1


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()

    calculate_ids(lines)
    print(find_highest_id())
    print(find_my_seat())


if __name__ == '__main__':
    main()
