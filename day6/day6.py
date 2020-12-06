# --- Day 6: Custom Customs ---
from util.parser import get_input_grouped

# --- Part One ---
def count_answers(data):
    counts = []
    for group in data:
        answers = set()
        for entry in group:
            answers = answers.union(set(entry))
        counts.append(len(answers))
        answers.clear()
    return counts

def sum_answers(data):
    return sum(count_answers(data))

# --- Part Two ---
def part_two(lines):
    count = 0
    return count


def main():
    data = get_input_grouped()
    print(sum_answers(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
