from utils.api import get_input


def get_rugsack_groups(rugsacks):
    for i in range(0, len(rugsacks), 3):
        yield rugsacks[i:i + 3]


def find_common_item_in_sack(rugsack):
    half_point_in_rugsack = int(len(rugsack)/2)
    first_compartment = rugsack[:half_point_in_rugsack]
    second_compartment = rugsack[half_point_in_rugsack:]

    for item in first_compartment:
        if item in second_compartment:
            return item
    
    print(f"No common item in rugsack: {rugsack}")
    exit()


def find_common_item_in_rugsack_group(rugsack_group):
    for item in rugsack_group[0]:
        if item in rugsack_group[1] and item in rugsack_group[2]:
            return item

    print(f"No common item in rugsack group: {rugsack_group}")
    exit()
    

def get_item_priority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


input_str = get_input(3)

rugsacks = input_str.rstrip().split("\n")

wrongfully_placed_items = [
    find_common_item_in_sack(rugsack)
    for rugsack
    in rugsacks
]

part_1_result = sum([get_item_priority(item) for item in wrongfully_placed_items])

print(f"Solution part 1: {part_1_result}")


badges = [
    find_common_item_in_rugsack_group(rugsack_group)
    for rugsack_group
    in get_rugsack_groups(rugsacks)
]

part_2_result = sum([get_item_priority(item) for item in badges])

print(f"Solution part 2: {part_2_result}")