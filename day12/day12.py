# --- Day 12: Rain Risk ---
from util.parser import get_input_lines


# --- Part One ---
def part_one(data):
    count = 0
    return count


class Ship(object):
    compass = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}

    def __init__(self, bearing: int = 90) -> None:
        self.bearing = bearing

    def turn_left(self, degrees: int):
        self.turn(-degrees)

    def turn_right(self, degrees: int):
        self.turn(degrees)

    def turn(self, degrees: int):
        self.bearing = (self.bearing + degrees) % 360

    def direction(self) -> str:
        base = 90
        nearest = base * round(self.bearing / base)
        return Ship.compass.get(nearest)

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
