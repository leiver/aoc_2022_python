from utils.api import get_input
import numpy

delta = {
    "U": numpy.array([0, 1]),
    "R": numpy.array([1, 0]),
    "D": numpy.array([0, -1]),
    "L": numpy.array([-1, 0])
}


def simulate_head_and_tails_from_commands(commands: list, tails: int):
    head_and_tail_coordinates = [numpy.array([0, 0]) for _ in range(tails + 1)]
    visited_positions = {(0, 0)}

    for command in commands:
        direction, steps = command.rstrip().split(" ")
        for _ in range(int(steps)):
            head_and_tail_coordinates[0] += delta[direction]

            for i in range(1, len(head_and_tail_coordinates)):
                difference = (
                    head_and_tail_coordinates[i - 1]
                    - head_and_tail_coordinates[i]
                )

                if abs(difference[0]) > 1 or abs(difference[1]) > 1:
                    tail_delta = numpy.array([
                        int(difference_vector / max(abs(difference_vector), 1))
                        for difference_vector in difference
                    ])
                    head_and_tail_coordinates[i] += tail_delta

            visited_positions.add(tuple(head_and_tail_coordinates[-1]))

    return len(visited_positions)


commands = get_input(9).rstrip().split("\n")

print(f"Solution part 1: {simulate_head_and_tails_from_commands(commands, 1)}")

print(f"Solution part 2: {simulate_head_and_tails_from_commands(commands, 9)}")
