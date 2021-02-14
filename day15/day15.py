# --- Day 15: Rambunctious Recitation ---
from collections import Iterable

from util.parser import get_input_lines


# --- Part One ---
class Game(object):
    def __init__(self, data: Iterable) -> None:
        self.turn = 0  # current turn
        self.memory = {}  # saves the round a number was spoken
        self.starting = [int(x) for x in data]  # starting numbers
        self.last = None  # last number spoken

    def memorize(self, num: int, val: int):
        self.memory[num] = val

    def play_turn(self):
        self.turn += 1
        if self.starting:
            num = self.starting.pop(0)
            self.memorize(num, self.turn)
        else:
            num = self.last
            if num in self.memory:
                mem = self.memory[num]
                self.memorize(num, self.turn-1)
                num = self.turn-1 - mem
            else:
                self.memorize(num, self.turn-1)
                num = 0
        self.last = num
        return num


def part_one(data: Iterable) -> int:
    game = Game(data)
    while game.turn < 2019:
        game.play_turn()
    return game.play_turn()


# --- Part Two ---
def part_two(data: Iterable):
    count = 0
    return count


def main():
    data = (get_input_lines()[0].split(","))
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
