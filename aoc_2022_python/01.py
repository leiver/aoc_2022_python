from utils.api import get_input

calories = [
    sum(map(int, food_list.split("\n")))
    for food_list
    in get_input(1).rstrip().split("\n\n")
]
calories.sort(reverse=True)

print(f"Solution part 1: {calories[0]}")
print(f"Solution part 2: {calories[0] + calories[1] + calories[2]}")
