from utils.api import get_input
from itertools import permutations
from queue import Queue
from multiprocessing.pool import ThreadPool

threadpool = ThreadPool(processes=10000)

input_str = get_input(16)

valve_map = {}
relevant_valves = set()

for line in input_str.strip().split("\n"):
    valve, tunnels = [part.split(" ") for part in line.strip().split("; ")]
    tunnels = [tunnel.strip(",") for tunnel in tunnels[4:]]
    flow_rate = int(valve[4][5:])
    valve = valve[1]

    valve_map[valve] = {
        "valve": valve,
        "flow_rate": flow_rate,
        "tunnels": set(tunnels)
    }

    if flow_rate > 0:
        relevant_valves.add(valve)

cost_map = {
    valve["valve"]: {neighbour_valve: 1 for neighbour_valve in valve["tunnels"]}
    for valve
    in valve_map.values()
}

for valve in valve_map.keys():
    queue = Queue()
    visited_valves = {valve}
    queue.put((0, valve))
    while not queue.empty():
        current_cost, current_valve = queue.get()
        cost_map[valve][current_valve] = current_cost
        for neighbour_valve in valve_map[current_valve]["tunnels"] - visited_valves:
            queue.put((current_cost+1, neighbour_valve))
            visited_valves.add(current_valve)

# for intermidiate_node in valve_map.keys():
#     for start_node in valve_map.keys():
#         for end_node in valve_map.keys():
#             if intermidiate_node in cost_map[start_node] and end_node in cost_map[intermidiate_node]:
#                 if (end_node not in cost_map[start_node] or cost_map[start_node][end_node] > cost_map[start_node][intermidiate_node] + cost_map[intermidiate_node][end_node]):
#                     cost_map[start_node][end_node] = cost_map[start_node][intermidiate_node] + cost_map[intermidiate_node][end_node]

# for start_valve in cost_map.keys():
#     print(f"{start_valve} -> {cost_map[start_valve]}")


def find_highest_pressure_release(
    current_node,
    current_score,
    remaining_valves,
    remaining_time
):
    current_score = (
        current_score
        + valve_map[current_node]["flow_rate"]
        * remaining_time
    )
    highest_score_found = current_score
    for next_valve in remaining_valves:
        if cost_map[current_node][next_valve] + 1 <= remaining_time:
            next_score = find_highest_pressure_release(
                next_valve,
                current_score,
                remaining_valves - {next_valve},
                remaining_time - cost_map[current_node][next_valve] - 1
            )
            highest_score_found = max(highest_score_found, next_score)

    return highest_score_found


highest_pressure_release = find_highest_pressure_release(
    "AA",
    0,
    relevant_valves,
    30
)

print(f"Solution day 1: {highest_pressure_release}")

# remaining_valves = relevant_valves.copy()
# remaining_time = 30
# current_valve = "AA"
# total_pressure_released = 0
# while len(remaining_valves) > 0:
#     highest_pressure_release_option = -1
#     for valve in remaining_valves:
#         pressure_released = (remaining_time - cost_map[current_valve][valve] - 1) * valve_map[valve]["flow_rate"]
#         if pressure_released > highest_pressure_release_option:
#             highest_pressure_release_option = pressure_released
#             best_valve = valve
#     if highest_pressure_release_option == -1:
#         break
#     remaining_valves.remove(best_valve)
#     total_pressure_released += highest_pressure_release_option
#     remaining_time -= cost_map[current_valve][best_valve] + 1
#     current_valve = best_valve

# print(f"Solution day 1: {total_pressure_released}")


def find_highest_pressure_release_with_elephant(
    valves_and_times,
    current_score,
    remaining_valves
):
    if len(valves_and_times) == 0:
        return current_score

    current_score = current_score + sum(
        [
            valve_map[valve]["flow_rate"] * remaining_time
            for valve, remaining_time
            in valves_and_times
        ]
    )

    results = []
    for valves in permutations(remaining_valves, len(valves_and_times)):
        next_valves_and_times = []
        valves_to_go_to = set()
        for next_valve, (current_valve, remaining_time) in zip(valves, valves_and_times):
            if cost_map[current_valve][next_valve] + 1 <= remaining_time:
                next_valves_and_times.append((
                    next_valve,
                    remaining_time - cost_map[current_valve][next_valve] - 1
                ))
                valves_to_go_to.add(next_valve)

        results.append(threadpool.apply_async(
            lambda: find_highest_pressure_release_with_elephant(
                valves_and_times,
                current_score,
                remaining_valves - valves_to_go_to
            )
        ))

        # highest_pressure_release = max(
        #     find_highest_pressure_release_with_elephant(
        #         valves_and_times,
        #         current_score,
        #         remaining_valves - valves_to_go_to
        #     ),
        #     highest_pressure_release
        # )

    return max([result.get() for result in results])


highest_pressure_release = find_highest_pressure_release_with_elephant(
    [
        ("AA", 26),
        ("AA", 26)
    ],
    0,
    relevant_valves
)

print(f"Solution day 2: {highest_pressure_release}")
