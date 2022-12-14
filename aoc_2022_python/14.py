from utils.api import get_input
from utils.api import sliding_window
from utils.api import divide_safely_with_0
import numpy


SAND_START_POINT = numpy.array([500, 0])
DIAGONALS = [numpy.array([-1, 1]), numpy.array([1, 1])]

blockers = set()
sand = set()
columns = {}
bottom_of_map = 0


def add_to_map(pos):
    blockers.add(tuple(pos))
    if pos[0] not in columns:
        columns[pos[0]] = {pos[1]}
    else:
        columns[pos[0]].add(pos[1])


def read_map():
    blockers.clear()
    sand.clear()
    columns.clear()
    for path in get_input(14).strip().split("\n"):
        points = [
            numpy.array([int(coord) for coord in point.split(",")])
            for point
            in path.strip().split(" -> ")
        ]
        for start, end in sliding_window(points, 2):
            difference = end - start
            abs_difference = numpy.abs(difference)
            delta = divide_safely_with_0(difference, abs_difference)
            current_pos = start
            add_to_map(start)
            for _ in range(max(abs_difference)):
                current_pos = delta + current_pos
                add_to_map(current_pos)

    return max([blocker[1] for blocker in blockers]) + 2


def print_map():
    x_min = min(list(columns.keys()))
    x_max = max(list(columns.keys()))
    y_min = 0
    y_max = max([blocker[1] for blocker in blockers])
    if len(sand) > 0:
        y_max = max(y_max, max([blocker[1] for blocker in blockers]))
    print(f"{x_min} -> {x_max}")
    print(f"{y_min} -> {y_max}")
    for y in range(y_min, y_max+1):
        print(
            str(y).ljust(3) + ''.join(
                [
                    "+" if (x, y) == (500, 0) else "#" if (x, y) in blockers else ("o" if (x, y) in sand else ".")
                    for x
                    in range(x_min, x_max+1)
                ]
            )
        )


def add_sand_to_map(pos):
    sand.add(tuple(pos))
    if pos[0] not in columns:
        columns[pos[0]] = {pos[1]}
    else:
        columns[pos[0]].add(pos[1])


def drop_sand(sand_pos, part=1):
    walls_under_sand = list(filter(
        lambda wall: wall > sand_pos[1],
        columns[sand_pos[0]]
    ))
    if len(walls_under_sand) == 0:
        if part == 1:
            return False
        else:
            add_sand_to_map([sand_pos[0], bottom_of_map - 1])
            return True
    landing_spot = numpy.array([sand_pos[0], min(walls_under_sand)-1])
    for diagonal in DIAGONALS:
        diagonal = landing_spot + diagonal
        if tuple(diagonal) not in blockers and tuple(diagonal) not in sand:
            if diagonal[0] not in columns:
                if part == 1:
                    return False
                else:
                    add_sand_to_map([diagonal[0], bottom_of_map - 1])
                    return True
            return drop_sand(diagonal, part)
    if tuple(landing_spot) == tuple(SAND_START_POINT) and part == 2:
        return False
    add_sand_to_map(landing_spot)
    return True


bottom_of_map = read_map()
sand_dropped = 0
while drop_sand(SAND_START_POINT):
    sand_dropped += 1

print(f"Solution part 1: {sand_dropped}")

bottom_of_map = read_map()
sand_dropped = 0
while drop_sand(SAND_START_POINT, part=2):
    sand_dropped += 1

print(f"Solution part 2: {sand_dropped+1}")
