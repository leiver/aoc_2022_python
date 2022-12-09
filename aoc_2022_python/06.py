from utils.api import get_input


def sliding_window(list, length):
    for i in range(0, len(list) - length):
        yield list[i:i + length]


def find_first_sequence_with_no_duplicates(list, length):
    for window, index in zip(sliding_window(list, length), range(len(list))):
        if len(set(window)) == length:
            return index + length


input_str = get_input(6)

print(f"Solution part 1: {find_first_sequence_with_no_duplicates(input_str, 4)}")

print(f"Solution part 2: {find_first_sequence_with_no_duplicates(input_str, 14)}")
