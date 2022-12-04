from utils.api import get_input
import re

input_str = get_input(4)

fully_overlapping_elves = 0
partly_overlapping_elves = 0

for pair in input_str.rstrip().split("\n"):
    first_start, first_end, second_start, second_end = [int(num) for num in re.split(',|-', pair.rstrip())]

    if (first_start <= second_start and first_end >= second_end) or (second_start <= first_start and second_end >= first_end):
        fully_overlapping_elves += 1
    
    if first_start <= second_end and first_end >= second_start:
        partly_overlapping_elves += 1

print(f"Solution part 1: {fully_overlapping_elves}")

print(f"Solution part 2: {partly_overlapping_elves}")