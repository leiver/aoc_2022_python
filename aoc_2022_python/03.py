from utils.api import get_input


def get_rugsack_groups(rugsacks):
    for i in range(0, len(rugsacks), 3):
        yield rugsacks[i:i + 3]


def find_common_item_for_sacks(rugsacks):
    result = set(rugsacks[0])
    for i in range(1, len(rugsacks)):
        result = result.intersection(set(rugsacks[i]))
    
    return result.pop()


def get_item_priority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


rugsacks = get_input(3).rstrip().split("\n")

part_1_result = sum(
    [
        get_item_priority(
            find_common_item_for_sacks(
                [
                    rugsack[:int(len(rugsack)/2)],
                    rugsack[int(len(rugsack)/2):]
                ]
            )
        )
        for rugsack in rugsacks
    ]
)
print(f"Solution part 1: {part_1_result}")

part_2_result = sum([
    get_item_priority(find_common_item_for_sacks(rugsack_group))
    for rugsack_group
    in get_rugsack_groups(rugsacks)
])

print(f"Solution part 2: {part_2_result}")