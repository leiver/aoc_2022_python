from utils.api import get_input

from enum import Enum

class GameResult(Enum):
    LOSS = 0
    TIE = 3
    WIN = 6

hand_mapping = {
    "X": "A", 
    "Y": "B", 
    "Z": "C"
}

hand_score_mapping = {
    "A": 1, 
    "B": 2, 
    "C": 3
}

possible_hands = ["A", "B", "C"]

game_result_order = [GameResult.TIE, GameResult.LOSS, GameResult.WIN]

strategy_mapping = {"X": -1, "Y": 0, "Z": 1}


def determine_score_for_round(round):
    hands = round.rstrip().split(" ")
    first_player = hands[0]
    second_player = hands[1]
    if second_player in hand_mapping:
        second_player = hand_mapping[hands[1]]

    game_result = game_result_order[(3 + hand_score_mapping[first_player] - hand_score_mapping[second_player]) % 3]
    
    return hand_score_mapping[second_player] + game_result.value


def map_round_by_part_2_strategy(round):
    (first_player, strategy) = round.rstrip().split(" ")
    second_player = possible_hands[(3 + hand_score_mapping[first_player]-1 + strategy_mapping[strategy]) % 3]

    return f"{first_player} {second_player}"


input_str = get_input(2)

resulting_score_part_1 = sum(
    [
        determine_score_for_round(round)
        for round
        in input_str.rstrip().split("\n")
    ]
)

print(f"Solution part 1: {resulting_score_part_1}")


resulting_score_part_2 = sum(
    [
        determine_score_for_round(map_round_by_part_2_strategy(round))
        for round
        in input_str.rstrip().split("\n")
    ]
)

print(f"Solution part 2: {resulting_score_part_2}")