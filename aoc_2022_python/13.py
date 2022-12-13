from utils.api import get_input
from functools import cmp_to_key

def compare_list(left, right):
    for left_part, right_part in zip(left, right):
        if isinstance(left_part, int) and isinstance(right_part, int):
            if left_part != right_part:
                return right_part - left_part
        else:
            left_part = [left_part] if isinstance(left_part, int) else left_part
            right_part = [right_part] if isinstance(right_part, int) else right_part

            compared_lists = compare_list(left_part, right_part)
            if compared_lists != 0:
                return compared_lists
    return len(right) - len(left)


solution_part_1 = 0
packets = []

for index, pair in enumerate(get_input(13).strip().split("\n\n")):
    left, right = [eval(packet) for packet in pair.strip().split("\n")]

    if compare_list(left, right) > 0:
        solution_part_1 += index+1

    packets += [left, right]

print(f"Solution part 1: {solution_part_1}")

packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare_list), reverse=True)

divider_packets = (packets.index([[2]])+1) * (packets.index([[6]])+1)

print(f"Solution part 2: {divider_packets}")
