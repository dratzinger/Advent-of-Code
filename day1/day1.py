# --- Day 1: Report Repair ---

# --- Part One ---
def compare_all(i, j):
    if j + i == 2020:
        return j * i


def brute_force(numbers):
    for i in numbers:
        for j in numbers:
            result = compare_all(i, j)
            if result:
                return result


# --- Part Two ---
def compare_three(i, j, k):
    if i + j + k == 2020:
        return i * j * k


def brute_force_three(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                result = compare_three(i, j, k)
                if result:
                    return result


def int_list(strings):
    numbers = []
    for i in strings:
        numbers.append(int(i))
    return numbers


def main():
    f = open('input.txt')
    lines = f.readlines()
    f.close()

    numbers = int_list(lines)

    print(brute_force(numbers))
    print(brute_force_three(numbers))


if __name__ == '__main__':
    main()
