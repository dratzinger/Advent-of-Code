# --- Day 8: Handheld Halting ---
from typing import List, Tuple

from util.parser import get_input_lines


class Program(object):
    def __init__(self, instructions: List[str]) -> None:
        self.instructions = instructions
        self.executed = [False] * len(instructions)
        self.accumulator = 0
        self.pointer = 0

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
            if self.executed[self.pointer]:
                break
            self.__execd(self.pointer)
            self.OPS.get(op)(arg)
        return self.accumulator

    def __acc(self, num: int):
        self.accumulator += num
        self.pointer += 1

    def __jmp(self, num: int):
        self.pointer += num

    def __nop(self, num: int):
        self.pointer += 1

    def __execd(self, pointer: int):
        self.executed[pointer] = True


# --- Part One ---
def check_loop_acc_state(data):
    return Program(data).run()


# --- Part Two ---
def check_final_acc_state(data):
    count = 0
    return count


def main():
    data = get_input_lines()
    print(check_loop_acc_state(data))
    print(check_final_acc_state(data))


if __name__ == '__main__':
    main()
