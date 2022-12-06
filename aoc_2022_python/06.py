from utils.api import get_input
from collections import deque


def list_contains_no_duplicates(list):
    copied_list = list.copy()
    for i in range(len(list))[::-1]:
        copied_list.pop()
        if list[i] in copied_list:
            return False

    return True


input_str = get_input(6)

current_signal_count = 0
start_of_packet_queue = deque()
start_of_message_queue = deque()
start_of_packet = 0
start_of_message = 0
for signal in input_str:
    if len(start_of_packet_queue) == 4:
        start_of_packet_queue.popleft()
    if len(start_of_message_queue) == 14:
        start_of_message_queue.popleft()

    start_of_packet_queue.append(signal)
    start_of_message_queue.append(signal)

    current_signal_count += 1

    if (
        len(start_of_packet_queue) == 4
        and list_contains_no_duplicates(start_of_packet_queue)
        and start_of_packet == 0
    ):
        start_of_packet = current_signal_count
    if (
        len(start_of_message_queue) == 14
        and list_contains_no_duplicates(start_of_message_queue)
        and start_of_message == 0
    ):
        start_of_message = current_signal_count

    if start_of_message > 0 and start_of_packet > 0:
        break

print(f"Solution part 1: {start_of_packet}")

print(f"Solution part 2: {start_of_message}")
