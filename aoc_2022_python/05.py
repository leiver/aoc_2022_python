from utils.api import get_input

input_str = get_input(5)

stacks_part_1 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

stacks_part_2 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

for row in input_str.rstrip().split("\n"):
    if row.startswith(" ") or row.startswith("["):
        for i in range(0, 9):
            if row[i * 4 + 1] != " ":
                stacks_part_1[i + 1].append(row[i * 4 + 1])
                stacks_part_2[i + 1].append(row[i * 4 + 1])

    if not row.rstrip():
        for i in range(1, 10):
            stacks_part_1[i].reverse()
            stacks_part_2[i].reverse()

    if row.startswith("move"):
        _, amount, _, from_stack, _, to_stack = row.rstrip().split(" ")
        amount, from_stack, to_stack = map(int, [amount, from_stack, to_stack])

        for i in range(amount):
            stacks_part_1[to_stack].append(stacks_part_1[from_stack].pop())

        for package in stacks_part_2[from_stack][-amount : len(stacks_part_2[from_stack])]:
            stacks_part_2[to_stack].append(package)
        stacks_part_2[from_stack] = stacks_part_2[from_stack][:-amount]


top_of_each_stack_part_1 = "".join(
    [stacks_part_1[stack_index][-1] for stack_index in range(1, 10)]
)

print(f"Solution part 1: {top_of_each_stack_part_1}")

top_of_each_stack_part_2 = "".join(
    [stacks_part_2[stack_index][-1] for stack_index in range(1, 10)]
)

print(f"Solution part 2: {top_of_each_stack_part_2}")
