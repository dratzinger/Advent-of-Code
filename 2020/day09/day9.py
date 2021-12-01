# --- Day 9: Encoding Error ---
from util.parser import get_input_lines


# --- Part One ---
def part_one(data, preamble_length: int):
    return first_invalid(data, preamble_length)


def first_invalid(data: [], preamble_length: int):
    numbers = [int(num) for num in data]
    invalid = find_invalid(numbers, preamble_length)
    first = next(invalid)
    return first


def find_invalid(data: [], preamble_length: int):
    for i in range(preamble_length, len(data)):  # skip iterating the preamble
        offset = 0 if i < preamble_length else i - preamble_length
        indices = (i for i in range(offset, i))
        preamble = {data[index] for index in indices}
        num = data[i]
        if not valid(preamble, num):
            yield num


def valid(preamble: {}, target: int):
    for i in preamble:
        check = i - target
        if check in preamble or abs(check) in preamble:
            return True
    return False


# --- Part Two ---
def part_two(data, target: int):
    numbers = [int(num) for num in data if int(num) != target]
    contiguous = find_contiguous(numbers, target)
    return min(contiguous) + max(contiguous)


def find_contiguous(data, target: int):
    while len(data) > 1:
        for (index, total) in sum_sequentially(data):
            if total == target:
                return data[:index+1]
            elif total > target:
                data = data[1:]
                break


def sum_sequentially(data):
    total = 0
    for i in range(0, len(data)):
        total += data[i]
        yield i, total


def main():
    data = get_input_lines()
    solution_one = part_one(data, 25)
    print(solution_one)
    print(part_two(data, solution_one))


if __name__ == '__main__':
    main()
