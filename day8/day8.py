# --- Day 8: Handheld Halting ---
from copy import deepcopy
from typing import List

from util.parser import get_input_lines


class Program(object):
    def __init__(self, instructions: List[str]) -> None:
        self.instructions = instructions
        self.executed = [False] * len(instructions)
        self.jump_stack = []
        self.accumulator = 0
        self.pointer = 0

        self.OPS = {
            "acc": self.__acc,
            "jmp": self.__jmp,
            "nop": self.__nop
        }

    def run(self) -> int:
        while not self.run_completed():
            inst = self.instructions[self.pointer].split()
            op: str = inst[0]
            arg: int = int(inst[1])
            if self.executed[self.pointer]:
                break
            self.__execd(self.pointer)
            self.OPS.get(op)(arg)
        return self.accumulator

    def run_completed(self):
        return self.pointer+1 >= len(self.instructions)

    def __acc(self, num: int):
        self.accumulator += num
        self.pointer += 1

    def __jmp(self, num: int):
        self.jump_stack.append(self.pointer)
        self.pointer += num

    def __nop(self, num: int):
        self.pointer += 1

    def __execd(self, pointer: int):
        self.executed[pointer] = True


class JumpLoopRemover(object):
    def __init__(self, p: Program) -> None:
        self.program = p

    def troubleshoot(self):
        self.program.run()
        loop_removed = self.program.run_completed()
        stack = self.program.jump_stack
        while len(stack) > 0 and not loop_removed:
            change_no = stack.pop()
            p = self.altered_program_copy(change_no, "nop +0")
            acc = p.run()
            loop_removed = p.run_completed()
            if loop_removed:
                return acc
        return "failed to establish a running state by changing single jump"

    def altered_program_copy(self, instruction_no: int, change_to: str):
        copy = deepcopy(self.program)
        copy.instructions[instruction_no] = change_to
        return copy


# --- Part One ---
def check_loop_acc_state(data):
    return Program(data).run()


# --- Part Two ---
def check_final_acc_state(data):
    watcher = JumpLoopRemover(Program(data))
    return watcher.troubleshoot()


def main():
    data = get_input_lines()
    print(check_loop_acc_state(data))
    print(check_final_acc_state(data))


if __name__ == '__main__':
    main()
