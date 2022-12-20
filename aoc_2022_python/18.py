from utils.api import get_input
import numpy
from queue import Queue

neighbours = [
    numpy.array([1, 0, 0]),
    numpy.array([-1, 0, 0]),
    numpy.array([0, -1, 0]),
    numpy.array([0, 1, 0]),
    numpy.array([0, 0, 1]),
    numpy.array([0, 0, -1])
]

input_str = get_input(18)

cubes = {}
air_cubes = {}
for cube in input_str.strip().split("\n"):
    cube = numpy.array([int(axis) for axis in cube.strip().split(",")])
    cube_tuple = tuple(cube)
    if cube_tuple in air_cubes:
        del air_cubes[cube_tuple]
    covered_sides = 0
    for neighbour in neighbours:
        neighbour = tuple(neighbour + cube)
        if neighbour in cubes:
            covered_sides += 1
            cubes[neighbour] += 1
        elif neighbour in air_cubes:
            air_cubes[neighbour] += 1
        else:
            air_cubes[neighbour] = 1

    cubes[cube_tuple] = covered_sides

surface_area = sum([6 - covered_sides for covered_sides in cubes.values()])

print(f"Solution part 1: {surface_area}")

bounds = (
    (min([cube[0] for cube in cubes.keys()]), max([cube[0] for cube in cubes.keys()])),
    (min([cube[1] for cube in cubes.keys()]), max([cube[1] for cube in cubes.keys()])),
    (min([cube[2] for cube in cubes.keys()]), max([cube[2] for cube in cubes.keys()]))
)

parsed_cubes = set()
inside_cubes = set()
for cube in air_cubes.keys():
    if cube in parsed_cubes:
        continue
    queue = Queue()
    queue.put(cube)
    parsed_cubes.add(cube)
    edge_found = False
    current_chunk = set()
    while not queue.empty():
        current_cube = queue.get()
        current_chunk.add(current_cube)
        current_cube_numpy = numpy.array(current_cube)
        for neighbour in neighbours:
            neighbour = tuple(neighbour + current_cube_numpy)
            if (
                bounds[0][0] > neighbour[0] or neighbour[0] > bounds[0][1] or
                bounds[1][0] > neighbour[1] or neighbour[1] > bounds[1][1] or
                bounds[2][0] > neighbour[2] or neighbour[2] > bounds[2][1]
            ):
                edge_found = True
            elif neighbour not in parsed_cubes:
                parsed_cubes.add(current_cube)
                queue.put(neighbour)

    if not edge_found:
        inside_cubes.update(current_chunk)

true_surface_area = surface_area - sum(
    map(
        lambda filtered_air_cube: filtered_air_cube[1],
        filter(
            lambda air_cube: air_cube[0] in inside_cubes,
            air_cubes.items()
        )
    )
)

print(f"Solution part 2: {true_surface_area}")
