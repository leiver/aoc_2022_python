from utils.api import get_input
from queue import Queue


class Part1Strategy:
    def __init__(self, end, elevation_map) -> None:
        self.end = end
        self.elevation_map = elevation_map

    def is_goal_reached(self, node):
        return node == self.end

    def can_get_to(self, current_pos, destination):
        return ord(self.elevation_map[current_pos]) - ord(self.elevation_map[destination]) > -2


class Part2Strategy:
    def __init__(self, elevation_map) -> None:
        self.elevation_map = elevation_map

    def is_goal_reached(self, node):
        return self.elevation_map[node] == "a"

    def can_get_to(self, current_pos, destination):
        return ord(self.elevation_map[destination]) - ord(self.elevation_map[current_pos]) > -2


neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def find_shortest_path(start, strategy, elevation_map):
    queue = Queue()
    added_to_queue = {start}
    queue.put(([start], start))
    end_found = False

    while not queue.empty() and not end_found:
        steps, current_pos = queue.get()
        for neighbour in neighbours:
            neighbour = (neighbour[0] + current_pos[0], neighbour[1] + current_pos[1])
            if neighbour in elevation_map and neighbour not in added_to_queue:
                if strategy.can_get_to(current_pos, neighbour):
                    if strategy.is_goal_reached(neighbour):
                        steps_to_finish = steps + [neighbour]
                        end_found = True
                        break
                    queue.put((steps + [neighbour], neighbour))
                    added_to_queue.add(neighbour)

    return steps_to_finish


input_str = get_input(12)

elevation_map = {}
for y, row in enumerate(input_str.strip().split("\n")):
    for x, node in enumerate(row.strip()):
        current_pos = (x, y)
        if node == "S":
            start = current_pos
            node = "a"
        elif node == "E":
            end = current_pos
            node = "z"

        elevation_map[current_pos] = node

print(
    f"Solution part 1: {len(find_shortest_path(start, Part1Strategy(end, elevation_map), elevation_map)) - 1}"
)

print(
    f"Solution part 2: {len(find_shortest_path(end, Part2Strategy(elevation_map), elevation_map)) - 1}"
)
