# --- Day 2: Password Philosophy ---
from math import prod


def prepare_string(line: str):
    return line.strip("\n")


# --- Part One ---
def count_trees(lines, move_right, move_down):
    count = 0
    pos_x = 0

    for line in lines[::move_down]:
        line = prepare_string(line)
        wrapping_pos = pos_x % len(line)
        if "#" == line[wrapping_pos]:
            count += 1

        pos_x += move_right
    return count


# --- Part Two ---
def check_slopes(lines, slopes):
    tree_counts = []
    for slope in slopes:
        tree_counts.append(count_trees(lines, slope[0], slope[1]))
    return prod(tree_counts)


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()
    move_right = 3
    move_down = 1

    print(count_trees(lines, move_right, move_down))

    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    print(check_slopes(lines, slopes))


if __name__ == '__main__':
    main()
