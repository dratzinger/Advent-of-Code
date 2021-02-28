# --- Day 22: Crab Combat ---
from typing import Iterable, List

from util.parser import get_input_grouped


class Player(object):
    def __init__(self, name: str, stack: List[int]) -> None:
        self.name = name
        self.stack = stack

    def __str__(self) -> str:
        return self.name + "'s deck: " + str(self.stack)

    def has_cards(self) -> bool:
        return bool(self.stack)

    def play_card(self) -> int:
        card = self.stack.pop(0)
        print(self.name + " plays: " + str(card))
        return card

    def win_cards(self, *cards: int):
        self.stack.extend(reversed(sorted(cards)))

    def score(self):
        weighted = (enumerate(reversed(self.stack), 1))
        scores = (card * weight for weight, card in weighted)
        return sum(scores)


class Game(object):
    def __init__(self, data: Iterable) -> None:
        self.round = 0
        self.players = Game.create_players(data)
        self.player1 = self.players[0]
        self.player2 = self.players[1]

    @staticmethod
    def create_players(data: Iterable[List[str]]) -> List[Player]:
        players = []
        for block in data:
            if block[0].startswith("Player"):
                new_player = Player(block.pop(0), [int(card) for card in block if card != ""])
                players.append(new_player)
        return players

    def simulate(self) -> int:
        while self.player1.has_cards() and self.player2.has_cards():
            self.play_round()

        print("\n\n== Post-game results ==")
        self.print_state()
        print()
        winner = self.player1 if self.player1.has_cards() else self.player2
        return winner.score()

    def print_state(self):
        print(self.player1)
        print(self.player2)

    def play_round(self):
        self.round += 1
        print("\n-- Round "+str(self.round)+" --")
        self.print_state()

        card_1 = self.player1.play_card()
        card_2 = self.player2.play_card()

        def win(player: Player):
            print(player.name+" wins the round!")
            player.win_cards(card_1, card_2)

        if card_1 >= card_2:
            win(self.player1)
        else:
            win(self.player2)


# --- Part One ---
def part_one(data: Iterable) -> int:
    game = Game(data)
    result = game.simulate()
    return result


# --- Part Two ---
def part_two(data: Iterable) -> int:
    return 0


def main():
    data =  (get_input_grouped("input.txt", ":"))
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
