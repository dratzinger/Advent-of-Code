import re
from typing import List

def get_input_lines(filename: str = 'input.txt') -> List[str]:
    lines = __read_file(filename).split("\n")
    return lines

def get_input_grouped(filename: str = 'input.txt',
                      block_delimiter: str = " ") -> List:
    grouped = []
    lines = __read_file(filename).split("\n\n")
    for line in lines:
        grouped.append(__input_blocks(line, block_delimiter))
    return grouped

def __input_blocks(lines, block_delimiter):
    return re.split(block_delimiter+'|\n',lines)

def __read_file(filename: str):
    f = open(filename)
    lines = f.read()
    f.close()
    return lines