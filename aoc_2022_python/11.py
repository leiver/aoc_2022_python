from utils.api import get_input
from math import prod
from utils.api import get_test_input


class MultiplyWithConstant:
    def __init__(self, constant) -> None:
        self.constant: int = constant

    def operation(self, worry_level: int):
        return worry_level * self.constant


class AddConstant:
    def __init__(self, constant) -> None:
        self.constant: int = constant

    def operation(self, worry_level: int):
        return worry_level + self.constant


class MultiplyWithSelf:
    def operation(self, worry_level: int):
        return worry_level * worry_level


class Monkey:
    def __init__(
        self, items, operation, divisibility_factor, if_true, if_false
    ) -> None:
        self.items: list = items
        self.operation = operation
        self.divisibility_factor: int = divisibility_factor
        self.if_true: int = if_true
        self.if_false: int = if_false
        self.inspected_items: int = 0

    def test(self, worry_level: int):
        return (
            self.if_true
            if worry_level % self.divisibility_factor == 0
            else self.if_false
        )

    def __str__(self) -> str:
        return f"""
items: {self.items}
inspected_items: {self.inspected_items}
operation: {self.operation}
% {self.divisibility_factor} -> {self.if_true} -> {self.if_false}
        """


def parse_monkey(monkey: str):
    _, starting_items, operation, test, if_true, if_false = [
        input.strip().split(" ") for input in monkey.split("\n")
    ]

    if operation[4] == "+":
        operation = AddConstant(int(operation[5]))
    elif operation[5] == "old":
        operation = MultiplyWithSelf()
    else:
        operation = MultiplyWithConstant(int(operation[5]))

    return Monkey(
        [int(item.strip(",")) for item in starting_items[2:]],
        operation.operation,
        int(test[3]),
        int(if_true[5]),
        int(if_false[5]),
    )


monkeys = [parse_monkey(monkey) for monkey in get_input(11).strip().split("\n\n")]

for _ in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            new_worry_level = int(monkey.operation(item) / 3)
            monkeys[monkey.test(new_worry_level)].items.append(new_worry_level)
        monkey.inspected_items += len(monkey.items)
        monkey.items = []

inspected_items = [monkey.inspected_items for monkey in monkeys]
inspected_items.sort(reverse=True)

print(f"Solution part 1: {prod(inspected_items[:2])}")


monkeys = [parse_monkey(monkey) for monkey in get_input(11).strip().split("\n\n")]
worry_cap = prod([monkey.divisibility_factor for monkey in monkeys])

for _ in range(10000):
    for monkey in monkeys:
        for item in monkey.items:
            new_worry_level = monkey.operation(item) % worry_cap
            monkeys[monkey.test(new_worry_level)].items.append(new_worry_level)
        monkey.inspected_items += len(monkey.items)
        monkey.items = []

inspected_items = [monkey.inspected_items for monkey in monkeys]
inspected_items.sort(reverse=True)

print(f"Solution part 1: {prod(inspected_items[:2])}")
