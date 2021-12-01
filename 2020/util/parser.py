import re
from typing import List


def get_input_lines(filename: str = 'input.txt') -> List[str]:
    return __read_without_trailing_newline(filename).split("\n")


def get_input_grouped(filename: str = 'input.txt', block_delimiter: str = " ") -> List[List[str]]:
    lines = (__read_without_trailing_newline(filename).split("\n\n"))
    return [__input_blocks(line, block_delimiter) for line in lines]


def __input_blocks(lines, block_delimiter) -> List[str]:
    return re.split(block_delimiter + '|\n', lines)


def __read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def __read_without_trailing_newline(filename: str) -> str:
    return __read_file(filename).rstrip("\n")
