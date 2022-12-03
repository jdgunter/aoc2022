"""Solution to AOC day 2."""

ROCK = object()
PAPER = object()
SCISSORS = object()

LOSE = 0
DRAW = 3
WIN = 6

opponent_move_map = {"A": ROCK, "B": PAPER, "C": SCISSORS}
player_move_map = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
round_result_map = {"X": LOSE, "Y": DRAW, "Z": WIN}
move_score_map = {ROCK: 1, PAPER: 2, SCISSORS: 3}
move_beats_move_map = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
move_is_beaten_by_move_map = {v: k for k, v in move_beats_move_map.items()}


def get_input():
    """Read problem input."""
    with open("day2_input.txt", encoding="utf-8") as f:
        return f.readlines()


def parse(problem_input):
    """Parse the problem input into a list of encrypted token pairs."""
    return [line.rstrip("\n").split(" ") for line in problem_input]


def round_score_part_1(left_token, right_token):
    """Compute the score for the current round using the part 1 encrpytion scheme."""
    opponent_move = opponent_move_map[left_token]
    player_move = player_move_map[right_token]
    if opponent_move is player_move:
        round_result_score = DRAW
    elif move_beats_move_map[player_move] is opponent_move:
        round_result_score = WIN
    else:
        round_result_score = LOSE
    return move_score_map[player_move] + round_result_score


def round_score_part_2(left_token, right_token):
    """Compute the score for the given round using the part 2 encryption scheme."""
    opponent_move = opponent_move_map[left_token]
    round_result = round_result_map[right_token]
    if round_result == DRAW:
        player_move_score = move_score_map[opponent_move]
    elif round_result == WIN:
        player_move_score = move_score_map[move_is_beaten_by_move_map[opponent_move]]
    else:
        player_move_score = move_score_map[move_beats_move_map[opponent_move]]
    return round_result + player_move_score
    

def count_score(rounds, round_score_fn):
    """Count the player's score given a list of rock-paper-scissors rounds."""
    return sum(round_score_fn(left_token, right_token) for left_token, right_token in rounds)
        

parsed_input = parse(get_input())
print(count_score(parsed_input, round_score_part_1))
print(count_score(parsed_input, round_score_part_2))
    