# --- Day 4: Passport Processing ---

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]


def split_into_pairs(line: str):
    pairs = []
    for pair in line.strip("\n").split(" "):
        pair = pair.split(":")
        if len(pair) == 2:
            pairs.append(pair)
    return pairs


# --- Part One ---
def part_one(lines):
    count = 0
    data = []
    lines_remaining = len(lines)
    for line in lines:
        lines_remaining -= 1
        pairs = split_into_pairs(line)
        data.extend(pairs)
        if len(pairs) < 1 or not lines_remaining:
            count += required_fields_present(data)
            data.clear()
    return count


def required_fields_present(data):
    missing = REQUIRED_FIELDS.copy()
    for pair in data:
        key = pair[0]
        if key in missing:
            missing.remove(key)
    return len(missing) == 0


# --- Part Two ---
def part_two(lines):
    count = 0
    return count


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()
