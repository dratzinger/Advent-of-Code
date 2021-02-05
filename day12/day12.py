# --- Day 12: Rain Risk ---
from collections import deque
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
    def __init__(self, ship: Ship = Ship()) -> None:
        self.ship = ship
        self.north = 0
        self.east = 0

    def move_forward(self, nav: 'Navigation', value: int):
        nav.execute(self.ship.direction(), value)

    def move_north(self, value: int):
        self.north += value

    def move_east(self, value: int):
        self.east += value

    def rotate_right(self, value: int):
        self.ship.turn(value)

    def rotate_left(self, value: int):
        self.ship.turn(-value)


class Navigation(object):
    def __init__(self, state: State = State()) -> None:
        self.state = state

    def execute(self, action: str, value: int):
        if action == 'F':
            self.state.move_forward(self, value)
        elif action == 'N':
            self.state.move_north(value)
        elif action == 'S':
            self.state.move_north(-value)
        elif action == 'E':
            self.state.move_east(value)
        elif action == 'W':
            self.state.move_east(-value)
        elif action == 'R':
            self.state.rotate_right(value)
        elif action == 'L':
            self.state.rotate_left(value)
        else:
            raise RuntimeWarning("unknown instruction: " + action + str(value))

    def calculate_distance(self):
        return abs(self.state.north) + abs(self.state.east)


def part_one(data):
    navigation = Navigation()
    for instruction in data:
        navigation.execute(instruction[:1], int(instruction[1:]))
    return navigation.calculate_distance()


# --- Part Two ---
class Waypoint(State):
    def __init__(self, ship: Ship = Ship()) -> None:
        super().__init__(ship)
        self.wp = deque([1, 10, 0, 0])  # [N, E, S, W]

    def move_forward(self, nav: Navigation, value: int):
        self.north += (self.wp[0] - self.wp[2]) * value
        self.east += (self.wp[1] - self.wp[3]) * value

    def move_north(self, value: int):
        self.wp[0] += value

    def move_east(self, value: int):
        self.wp[1] += value

    def rotate_right(self, value: int):
        self.wp.rotate(Waypoint._rotations(value))

    def rotate_left(self, value: int):
        self.wp.rotate(-Waypoint._rotations(value))

    @staticmethod
    def _rotations(angle: int):
        return round((angle % 360) / 90)


def part_two(data):
    navigation = Navigation(Waypoint())
    for instruction in data:
        navigation.execute(instruction[:1], int(instruction[1:]))
    return navigation.calculate_distance()


def main():
    data = get_input_lines("input.txt")
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
