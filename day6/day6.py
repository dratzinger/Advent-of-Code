# --- Day 6: Custom Customs ---
from util.parser import get_input_grouped

def count_answers(data, set_operation):
    counts = []
    for group in data:
        test = map(lambda entry: set(entry), group)
        answers = set_operation(*test)
        counts.append(len(answers))
        answers.clear()
    return counts

# --- Part One ---
def count_answers_any(data):
    return count_answers(data, set.union)

def sum_answers(data):
    return sum(count_answers_any(data))


# --- Part Two ---
def count_answers_common(data):
    return count_answers(data, set.intersection)

def sum_answers_common(data):
    return sum(count_answers_common(data))


def main():
    data = get_input_grouped()
    print(sum_answers(data))
    print(sum_answers_common(data))


if __name__ == '__main__':
    main()
