from utils.api import get_input
import numpy
from shapely import box

BOUND = numpy.array([0, 4000000])
CORNERS = [
    numpy.array([BOUND[0], BOUND[0]]),
    numpy.array([BOUND[0], BOUND[1]]),
    numpy.array([BOUND[1], BOUND[0]]),
    numpy.array([BOUND[1], BOUND[1]])
]
BOUND_BOX = box(
    CORNERS[0],
    CORNERS[1],
    CORNERS[2],
    CORNERS[3]
)
RELEVANT_Y = 2000000


def manhatten_distance(a, b):
    sum(numpy.abs(a - b))


def find_x_range_sensor_coverage_for_y(sensor, manhatten_distance_beacon, y):
    sensorless_area_count = abs(abs(y - sensor[1]) - manhatten_distance_beacon) * 2 + 1

    return (
        sensor[0]-int(sensorless_area_count / 2),
        sensor[0]+int(sensorless_area_count / 2)
    )


def manhatten_distance_closest_corner(sensor):
    return min([manhatten_distance(sensor, corner) for corner in CORNERS])


def find_relevant_y_values(sensor, manhatten_distance_beacon):
    sensor_box = box(
        sensor[0] - manhatten_distance_beacon,
        sensor[1] - manhatten_distance_beacon,
        sensor[0] + manhatten_distance_beacon,
        sensor[1] + manhatten_distance_beacon
    )
    # Sensor inside the bounds
    if (BOUND[0] <= sensor[0] <= BOUND[1] and BOUND[0] <= sensor[1] <= BOUND[1]):
        return range(
            max(BOUND[0], sensor[1] - manhatten_distance_beacon),
            min(BOUND[1], sensor[1] + manhatten_distance_beacon) + 1
        )
    elif (BOUND_BOX.intersects(sensor_box)):
        x_distance_from_bounds = 0 if BOUND[0] <= sensor[0] <= BOUND[1] else min(
            abs(sensor[0] - BOUND[0]),
            abs(sensor[0] - BOUND[1])
        )
        return range(
            max(
                BOUND[0],
                sensor[1] - manhatten_distance_beacon + x_distance_from_bounds
            ),
            min(
                BOUND[1],
                sensor[1] + manhatten_distance_beacon - x_distance_from_bounds
            ) + 1
        )
    return []


input_str = get_input(15)

sensors = [
    [
        numpy.array([
            int(coord.split("=")[1])
            for coord
            in coords.split(", ")
        ])
        for coords
        in sensor.strip("Sensor at ").split(": closest beacon is at ")
    ]
    for sensor
    in input_str.strip().split("\n")
]

covered_tiles = {}
for sensor, beacon in sensors:
    manhatten_distance_beacon = sum(numpy.abs(beacon - sensor))
    for y in find_relevant_y_values(sensor, manhatten_distance_beacon):
        x_range = (
            max(BOUND[0], sensor[0] - manhatten_distance_beacon + abs(y - sensor[1])),
            min(BOUND[1], sensor[0] + manhatten_distance_beacon - abs(y - sensor[1]))
        )
        if y not in covered_tiles:
            covered_tiles[y] = [x_range]
        else:
            new_ranges = []
            for old_range in covered_tiles[y]:
                if x_range[0] <= old_range[1] and x_range[1] >= old_range[0]:
                    x_range = (
                        min(x_range[0], old_range[0]),
                        max(x_range[1], old_range[1])
                    )
                else:
                    new_ranges.append(old_range)
            new_ranges.append(x_range)
            covered_tiles[y] = new_ranges

for y, ranges in covered_tiles.items():
    if len(ranges) == 2:
        x = max([x_range[0] for x_range in ranges]) + 1
        print(f"Solution part 2: {x * 4000000 + y}")
        break


#relevant_row = 2000000
#sensorless_areas_for_relevant_row = set()
#for sensor, beacon in sensors:
#    manhatten_distance = sum(numpy.abs(beacon - sensor))
#
#    if sensor[1] - manhatten_distance <= relevant_row <= sensor[1] + manhatten_distance:
#        x_range = find_x_range_sensor_coverage_for_y(sensor, manhatten_distance, relevant_row)
#
#        for x in range(x_range[0], x_range[1] + 1):
#            if beacon[1] != relevant_row or beacon[0] != x:
#                sensorless_areas_for_relevant_row.add(x)
#
#print(f"Solution part 1: {len(sensorless_areas_for_relevant_row)}")
