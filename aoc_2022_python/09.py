from utils.api import get_input

delta_x = {"U": 0, "R": 1, "D": 0, "L": -1}
delta_y = {"U": 1, "R": 0, "D": -1, "L": 0}


def simulate_head_and_tails_from_commands(commands: list, tails: int):
    head_and_tail_coordinates = [(0, 0) for _ in range(tails + 1)]
    visited_positions = {(0, 0)}

    for command in commands:
        direction, steps = command.rstrip().split(" ")
        for _ in range(int(steps)):
            head_and_tail_coordinates[0] = (
                head_and_tail_coordinates[0][0] + delta_x[direction],
                head_and_tail_coordinates[0][1] + delta_y[direction],
            )

            for i in range(1, len(head_and_tail_coordinates)):
                difference_x = (
                    head_and_tail_coordinates[i - 1][0]
                    - head_and_tail_coordinates[i][0]
                )
                difference_y = (
                    head_and_tail_coordinates[i - 1][1]
                    - head_and_tail_coordinates[i][1]
                )

                if abs(difference_x) > 1 or abs(difference_y) > 1:
                    head_and_tail_coordinates[i] = (
                        head_and_tail_coordinates[i][0]
                        + difference_x / max(abs(difference_x), 1),
                        head_and_tail_coordinates[i][1]
                        + difference_y / max(abs(difference_y), 1),
                    )

            visited_positions.add(head_and_tail_coordinates[-1])

    return len(visited_positions)


commands = get_input(9).rstrip().split("\n")

print(f"Solution part 1: {simulate_head_and_tails_from_commands(commands, 1)}")

print(f"Solution part 2: {simulate_head_and_tails_from_commands(commands, 9)}")
