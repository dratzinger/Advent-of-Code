# --- Day 8: Handheld Halting ---
from typing import List, Tuple

from util.parser import get_input_lines


class Program(object):
    def __init__(self, instructions: List[str]) -> None:
        self.instructions = instructions
        self.accumulator = 0
        self.pointer = 0
        self.jump = 0
        self.jumped = False

        self.OPS = {
            "acc": self.__acc,
            "jmp": self.__jmp,
            "nop": self.__nop
        }

    def run(self) -> int:
        while self.pointer < len(self.instructions):
            inst = self.instructions[self.pointer].split()
            op: str = inst[0]
            arg: int = int(inst[1])
            if op != "jmp":
                self.__inc()
            if self.jumped and not self.jump:
                break
            self.OPS.get(op)(arg)
        return self.accumulator

    def __acc(self, num: int):
        self.accumulator += num

    def __jmp(self, num: int):
        self.pointer += num
        self.jump += num
        self.jumped = True

    def __nop(self, num: int):
        return

    def __inc(self):
        if self.jumped:
            self.jump += 1
        self.pointer += 1


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
