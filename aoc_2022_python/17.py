from utils.api import get_input
import numpy

wind_push_seq = get_input(17) #">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

wind_push_mapping = {
    "<": numpy.array([-1, 0]),
    ">": numpy.array([1, 0])
}

gravity = numpy.array([0, -1])

rocks = [
    [
        numpy.array([0, 0]),
        numpy.array([1, 0]),
        numpy.array([2, 0]),
        numpy.array([3, 0])
    ],
    [
        numpy.array([1, 0]),
        numpy.array([0, 1]),
        numpy.array([1, 1]),
        numpy.array([2, 1]),
        numpy.array([1, 2])
    ],
    [
        numpy.array([0, 0]),
        numpy.array([1, 0]),
        numpy.array([2, 0]),
        numpy.array([2, 1]),
        numpy.array([2, 2])
    ],
    [
        numpy.array([0, 0]),
        numpy.array([0, 1]),
        numpy.array([0, 2]),
        numpy.array([0, 3])
    ],
    [
        numpy.array([0, 0]),
        numpy.array([0, 1]),
        numpy.array([1, 0]),
        numpy.array([1, 1])
    ]
]


def is_rock_crashing(rock_pos, rock_index, rock_map):
    for rock_piece in rocks[rock_index]:
        point_in_map = rock_pos + rock_piece
        if (
            0 > point_in_map[0] or 6 < point_in_map[0]
            or 0 > point_in_map[1]
            or tuple(point_in_map) in rock_map
        ):
            return True

    return False


def drop_rock(push_index, rock_index, rock_map, highest_point_on_map):
    rock_pos = numpy.array([2, highest_point_on_map + 4])
    while True:
        wind_push = wind_push_mapping[wind_push_seq[push_index]]
        if not is_rock_crashing(rock_pos + wind_push, rock_index, rock_map):
            rock_pos += wind_push
        push_index = (push_index + 1) % len(wind_push_seq)
        if not is_rock_crashing(rock_pos + gravity, rock_index, rock_map):
            rock_pos += gravity
        else:
            for rock_piece in rocks[rock_index]:
                point_in_map = rock_pos + rock_piece
                rock_map.add(tuple(point_in_map))
                highest_point_on_map = max(
                    highest_point_on_map,
                    point_in_map[1]
                )
            return push_index, highest_point_on_map


def print_rock_map(rock_map, highest_point):
    for y in range(highest_point, -1, -1):
        row = ''.join(
            [
                "#" if (x, y) in rock_map else "."
                for x
                in range(7)
            ]
        )
        print(f"|{row}|")
    print("+-------+")


highest_point = -1
push_index = 0
rock_index = 0
rock_map = set()
for _ in range(2022):
    push_index, highest_point = drop_rock(
        push_index,
        rock_index,
        rock_map,
        highest_point
    )
    rock_index = (rock_index + 1) % len(rocks)

print(f"Solution part 1: {highest_point+1}")
