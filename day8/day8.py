# --- Day 8: Handheld Halting ---
from typing import List, Tuple

from util.parser import get_input_lines


class Program(object):
    def __init__(self, instructions: List[str]) -> None:
        self.instructions = instructions
        self.accumulator = 0
        self.pointer = 0
        self.jump = 0

    def run(self) -> int:
        while self.pointer < len(self.instructions):
            if not self.jump and self.pointer > 0:
                break
            inst = self.instructions[self.pointer].split()
            self.OPS.get(inst[0])(int(inst[1]))
        return self.accumulator

    def __acc(self, num: int):
        self.pointer += 1
        self.accumulator += num

    def __jmp(self, num: int):
        self.pointer += num
        self.jump += num

    def __nop(self, num: int):
        self.pointer += 1

    OPS = {
        "acc": __acc,
        "jmp": __jmp,
        "nop": __nop
    }


# --- Part One ---
def check_loop_acc_state(data):
    return Program(data).run()


# --- Part Two ---
def part_two(data):
    count = 0
    return count


def main():
    data = get_input_lines()
    print(check_loop_acc_state(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
