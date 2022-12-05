from utils.api import get_input
from functools import reduce

input_str = get_input(1)

elf_calory_counts = [
    sum(
        map(
            lambda food: int(food.strip()), 
            food_list.strip().split("\n")
        )
    ) 
    for food_list 
    in input_str.strip().split("\n\n")
]

elf_calory_counts.sort(reverse=True)

print(f"Solution part 1: {str(elf_calory_counts[0])}")
print(f"Solution part 2: {str(elf_calory_counts[0] + elf_calory_counts[1] + elf_calory_counts[2])}")
