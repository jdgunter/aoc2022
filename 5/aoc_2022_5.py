"""Advent of Code day 5."""

import copy


def get_input():
    """Read problem input."""
    with open("day5_input.txt", encoding="utf-8") as f:
        return f.read()


def parse_stacks(stacks_string):
    """Parse the initial stack state."""
    stacks_string_lines = list(reversed(stacks_string.split("\n")))
    num_stacks = len([ch for ch in stacks_string_lines[0].split(" ") if ch != ""])
    stacks = [None] + [[] for _ in range(num_stacks)]
    line_length = len(stacks_string_lines[1])
    for line in stacks_string_lines[1:]:
        for stack_index in range(num_stacks):
            current_index = 1 + stack_index * 4
            if current_index > line_length:
                break
            crate = line[current_index]
            if crate != " ":
                stacks[stack_index + 1].append(crate)
    return stacks


def parse_moves(moves_string):
    """Parse the moves string."""
    moves = []
    for line in moves_string.split("\n"):
        words = line.split(" ")
        moves.append((int(words[1]), int(words[3]), int(words[5])))
    return moves


def parse(problem_input):
    """Parse the problem input into an initial stacks state and a list of moves."""
    stacks_string, moves_string = problem_input.split("\n\n")
    stacks = parse_stacks(stacks_string)
    moves = parse_moves(moves_string)
    return stacks, moves


def execute_moves_9000(initial_stacks, moves):
    """Execute the given moves on the initial stacks state, moving one crate at a time."""
    stacks = copy.deepcopy(initial_stacks)
    for move_count, move_from, move_to in moves:
        for _ in range(move_count):
            crate = stacks[move_from].pop()
            stacks[move_to].append(crate)
    return stacks


def execute_moves_9001(initial_stacks, moves):
    """Execute the given moves on the initial stacks state, moving multiple crates at a time."""
    stacks = copy.deepcopy(initial_stacks)
    for move_count, move_from, move_to in moves:
        crates = stacks[move_from][-move_count:]
        stacks[move_from][-move_count:] = []
        stacks[move_to].extend(crates)
    return stacks


def top_crates(stacks):
    """Get a string representing the top crates on the stacks."""
    return "".join(stack[-1] for stack in stacks[1:])


EXAMPLE_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def test():
    """Run tests."""
    parsed_stacks, parsed_moves = parse(EXAMPLE_INPUT)
    assert parsed_stacks == [None, ['Z', 'N'], ['M', 'C', 'D'], ['P']], parsed_stacks
    assert parsed_moves == [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)], parsed_moves
    top_crates_string_9000 = top_crates(execute_moves_9000(parsed_stacks, parsed_moves))
    top_crates_string_9001 = top_crates(execute_moves_9001(parsed_stacks, parsed_moves))
    assert top_crates_string_9000 == "CMZ", top_crates_string_9000
    assert top_crates_string_9001 == "MCD", top_crates_string_9001
    print("Tests passed!")


def main():
    """Solve AOC2022 day 5."""
    initial_stacks, moves = parse(get_input())
    print(top_crates(execute_moves_9000(initial_stacks, moves)))
    print(top_crates(execute_moves_9001(initial_stacks, moves)))


test()
main()
