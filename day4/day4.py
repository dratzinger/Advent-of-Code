# --- Day 4: Passport Processing ---
import re

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


def count_valid_records(lines, validation_function):
    count = 0
    data = []
    lines_remaining = len(lines)
    for line in lines:
        lines_remaining -= 1
        pairs = split_into_pairs(line)
        data.extend(pairs)
        if len(pairs) < 1 or not lines_remaining:
            count += validation_function(data)
            data.clear()
    return count


# --- Part One ---
def part_one(lines):
    return count_valid_records(lines, required_fields_present)


def required_fields_present(data):
    missing = REQUIRED_FIELDS.copy()
    for pair in data:
        key = pair[0]
        if key in missing:
            missing.remove(key)
    return len(missing) == 0


# --- Part Two ---
def part_two(lines):
    return count_valid_records(lines, required_fields_valid)


def required_fields_valid(data):
    valid = required_fields_present(data)
    for pair in data:
        valid *= FIELD_FUNCTIONS.get(pair[0])(pair[1])
    return valid


def valid_birth_year(year):
    return len(year) == 4 and 1920 <= int(year) <= 2002


def valid_issue_year(year):
    return len(year) == 4 and 2010 <= int(year) <= 2020


def valid_expiration_year(year):
    return len(year) == 4 and 2020 <= int(year) <= 2030


def valid_height(height):
    valid = False
    if len(height) < 2:
        return False
    else:
        unit = height[-2:]
        value = height[:-2]
        if unit == "cm":
            valid = 150 <= int(value) <= 193
        elif unit == "in":
            valid = 59 <= int(value) <= 76
    return valid


def valid_hair_color(color):
    return bool(re.search("^#[0-9a-f]{6}$", color))


def valid_eye_color(color):
    return len(color) == 3 and color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def valid_passport_id(id):
    return bool(re.search("^[0-9]{9}$", id))


def valid_country_id(id):
    return True


# validation function by field name
FIELD_FUNCTIONS = {
    "byr": valid_birth_year,
    "iyr": valid_issue_year,
    "eyr": valid_expiration_year,
    "hgt": valid_height,
    "hcl": valid_hair_color,
    "ecl": valid_eye_color,
    "pid": valid_passport_id,
    "cid": valid_country_id,
}


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()

    print(part_one(lines))
    print(part_two(lines))


if __name__ == '__main__':
    main()
