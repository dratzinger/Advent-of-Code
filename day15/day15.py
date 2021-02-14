# --- Day 15: Rambunctious Recitation ---
from typing import Iterable

from util.parser import get_input_lines


# --- Part One ---
class Game(object):
    def __init__(self, data: Iterable) -> None:
        self.turn = 0  # current turn
        self.memory = {}  # saves the round a number was spoken
        self.starting = [int(x) for x in data]  # starting numbers
        self.last = None  # last number spoken

    def play_turn(self):
        self.turn += 1
        if self.starting:
            number = self.starting.pop(0)
            self.memory[number] = self.turn
        else:
            number = self.last
            previous_turn = self.turn - 1
            if number in self.memory:
                recalled_turn = self.memory[number]
                self.memory[number] = previous_turn
                number = previous_turn - recalled_turn
            else:
                self.memory[number] = previous_turn
                number = 0
        self.last = number
        return number

    def play_until(self, turn: int):
        while self.turn < turn-1:
            self.play_turn()
        return self.play_turn()


def part_one(data: Iterable) -> int:
    game = Game(data)
    return game.play_until(2020)


# --- Part Two ---
def part_two(data: Iterable) -> int:
    game = Game(data)
    return game.play_until(30000000)


def main():
    data = (get_input_lines()[0].split(","))
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
