# --- Day 18: Operation Order ---
from typing import Iterable

from pyparsing import nestedExpr, Word, oneOf, nums, ZeroOrMore

from util.parser import get_input_lines


def parse_nested(expression: str) -> list:
    operators = oneOf("+ *")
    nested_braces = nestedExpr('(', ')', )
    combined = ZeroOrMore(Word(nums) | operators | nested_braces)
    return combined.parseString(expression).asList()


# --- Part One ---
def part_one(data: Iterable) -> int:
    expressions = (calculate(exp) for exp in data)
    return sum(expressions)


ops = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}


def calculate(expression: str) -> int:
    parsed = parse_nested(expression)
    return evaluate_expression(parsed)


def evaluate_expression(exp: list):
    left = exp.pop(0)
    result = int(left) if not isinstance(left, list) else evaluate_expression(left)

    while exp:
        op = ops.get(exp.pop(0))
        right = exp.pop(0)
        right = int(right) if not isinstance(right, list) else evaluate_expression(right)
        result = op(result, right)
    return result


# --- Part Two ---
def part_two(data: Iterable) -> int:
    expressions = (calculate_prioritized(exp) for exp in data)
    return sum(expressions)


def calculate_prioritized(expression: str) -> int:
    parsed = parse_nested(expression)
    prioritized = prioritize(parsed)
    return evaluate_expression(prioritized)


def prioritize(expression: list) -> list:
    expression = [x if not isinstance(x, list) else prioritize(x) for x in expression]
    prioritized = [expression.pop(0)]

    while expression:
        if len(expression) >= 2:
            op = expression.pop(0)
            if op == '+':
                prioritized.append([prioritized.pop(), op, expression.pop(0)])
            else:
                prioritized.extend([op, expression.pop(0)])
        else:
            prioritized.append(expression.pop(0))

    return prioritized


def main():
    data = (get_input_lines())
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
