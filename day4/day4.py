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
    for line in lines:
        pairs = split_into_pairs(line)
        if len(pairs) < 1:
            count += int(validate(data))
            data.clear()
        else:
            data.extend(pairs)
    return count


def validate(data):
    required = REQUIRED_FIELDS.copy()
    for pair in data:
        key = pair[0]
        if key in required:
            required.remove(key)
    return not len(required)


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
