# --- Day 12: Rain Risk ---
from collections import namedtuple
from util.parser import get_input_lines


# --- Part One ---
class Ship(object):
    compass = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

    def __init__(self, bearing: int = 90) -> None:
        self.bearing = bearing

    def turn(self, degrees: int):
        self.bearing = (self.bearing + degrees) % 360

    def direction(self) -> str:
        base = 90
        nearest = base * round(self.bearing / base)
        return Ship.compass.get(nearest)


class State(object):
    def __init__(self) -> None:
        self.ship = Ship()
        self.north = 0
        self.east = 0

    def move_north(self, value: int):
        self.north += value

    def move_east(self, value: int):
        self.east += value

    def execute(self, action: str, value: int):
        if action == 'F':
            action = self.ship.direction()

        if action == 'N':
            self.north += value
        elif action == 'S':
            self.north -= value
        elif action == 'E':
            self.east += value
        elif action == 'W':
            self.east -= value
        elif action == 'R':
            self.ship.turn(value)
        elif action == 'L':
            self.ship.turn(-value)
        else:
            raise RuntimeWarning("unknown instruction: "+action+str(value))

    def calculate_distance(self):
        return abs(self.north) + abs(self.east)


def part_one(data):
    navigation = State()
    for instruction in data:
        navigation.execute(instruction[:1], int(instruction[1:]))
    return navigation.calculate_distance()


# --- Part Two ---
def part_two(data):
    count = 0
    return count


def main():
    data = get_input_lines("input.txt")
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
