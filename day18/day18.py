# --- Day 18: Operation Order ---
from typing import Iterable

from pyparsing import nestedExpr, Word, oneOf, nums, ZeroOrMore

from util.parser import get_input_lines

# --- Part One ---
ops = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}


def calculate(expression: str):
    parsed = parse_nested(expression)

    def evaluate_expression(exp: list):
        left = exp.pop(0)
        result = int(left) if left is not list else evaluate_expression(left)

        while exp:
            op = ops.get(exp.pop(0))
            right = exp.pop(0)
            right = int(right) if right is not list else evaluate_expression(right)
            left = op(left, right)
        return result

    return evaluate_expression(parsed)



def parse_nested(expression: str):
    operators = oneOf("+ *")
    nested_braces = nestedExpr('(', ')', )
    combined = ZeroOrMore(Word(nums) | operators | nested_braces)
    return combined.parseString(expression).asList()


def part_one(data: Iterable) -> int:
    expressions = (calculate(exp) for exp in data)
    return sum(expressions)


# --- Part Two ---
def part_two(data: Iterable) -> int:
    return 0


def main():
    data = (get_input_lines())
    print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()