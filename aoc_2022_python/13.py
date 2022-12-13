from utils.api import get_input
from functools import cmp_to_key


def parse_list(list: iter):
    result = []
    for part in list:
        if part == "[":
            result.append(parse_list(list))
        elif part.isnumeric():
            next_part = next(list)
            if next_part.isnumeric():
                part += next_part
            result.append(int(part))
            if next_part == "]":
                return result
        elif part == "]":
            return result


def compare_list(left, right):
    left = iter(left)
    right = iter(right)
    while True:
        left_part = next(left, None)
        right_part = next(right, None)

        if left_part is None and right_part is not None:
            return 1
        elif right_part is None and left_part is not None:
            return -1
        elif left_part is None and right_part is None:
            return 0
        elif isinstance(left_part, int) and isinstance(right_part, int):
            if left_part < right_part:
                return 1
            elif right_part < left_part:
                return -1
        else:
            left_part = [left_part] if isinstance(left_part, int) else left_part
            right_part = [right_part] if isinstance(right_part, int) else right_part

            compared_lists = compare_list(left_part, right_part)

            if compared_lists != 0:
                return compared_lists


input_str = get_input(13)
right_order_pairs = []
packets = []

for index, pair in enumerate(input_str.strip().split("\n\n")):
    left, right = pair.strip().split("\n")
    left = parse_list(iter(left[1:]))
    right = parse_list(iter(right[1:]))

    compared = compare_list(left, right)

    if compared == 1:
        right_order_pairs.append(index+1)

    packets += [left, right]

print(f"Solution part 1: {sum(right_order_pairs)}")

packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare_list), reverse=True)

divider_packets = (packets.index([[2]])+1) * (packets.index([[6]])+1)

print(f"Solution part 2: {divider_packets}")
