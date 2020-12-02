# --- Day 2: Password Philosophy ---

def prepare_string(line):
    line: str
    strings = line.strip("\n").split(" ")
    limits = strings[0].split("-")
    char = strings[1].strip(":")
    string = strings[2]
    return [int(limits[0]), int(limits[1]), char, string]

def validate(parameters):
    min = parameters[0]
    max = parameters[1]
    char = parameters[2]
    count = parameters[3].count(char)
    return min <= count <= max

# --- Part One ---
def count_valid_passwords(lines):
    count = 0
    for line in lines:
        parameters = prepare_string(line)
        if validate(parameters):
            count += 1
    return count

# --- Part Two ---


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()

    print(count_valid_passwords(lines))


if __name__ == '__main__':
    main()
