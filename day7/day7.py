# --- Day 7: Handy Haversacks ---
import re
from typing import Dict, List
from util.parser import get_input_lines


class Bag(object):
    contained_in = None

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def has_parent(self) -> bool:
        return bool(self.contained_in)

    def add_parent(self, bag):
        if not self.contained_in:
            self.contained_in = [bag]
        else:
            self.contained_in.append(bag)


def build_ruleset(lines) -> dict:
    bags: Dict[str, Bag] = dict()
    sep = ":"
    pattern = "( bags? ?(contain )? ?(, )?\.?)"
    for line in lines:
        rule = re.sub(pattern, sep, line).rstrip(sep).split(":")
        for bag in rule[1:]:
            parent_str = rule[0]
            if bag != "no other":
                child_str = bag[2:]
                child = bags.get(child_str)
                parent = bags.get(parent_str)
                if not parent:
                    parent = Bag(parent_str)
                    bags[parent_str] = parent
                if not child:
                    child = Bag(child_str)
                    bags[child_str] = child
                child.add_parent(parent)
    return bags


# --- Part One ---
def count_containing_rules(lines, contains_bag: str = "shiny gold"):
    bags = build_ruleset(lines)
    start = bags.get(contains_bag)
    return find_parents_recursive(start)


def find_parents_recursive(start: Bag):
    if not start.has_parent():
        return 1
    else:
        count = 0
        for parent in start.contained_in:
            count += find_parents_recursive(parent)
        return count


# --- Part Two ---
def part_two(lines):
    count = 0
    return count


def main():
    data = get_input_lines()
    print(count_containing_rules(data))
    print(part_two(data))


if __name__ == '__main__':
    main()
