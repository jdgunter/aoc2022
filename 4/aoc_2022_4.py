
"""Advent of Code day 4."""

def get_input():
    """Read problem input."""
    with open("day4_input.txt", encoding="utf-8") as f:
        return f.readlines()


def assignment_set_from_string(section_range_string):
    """Construct the set of assigned section IDs from a section range string."""
    start, end_inclusive = map(int, section_range_string.split("-"))
    return set(range(start, end_inclusive+1))


def parse(problem_input):
    """Parse the problem input into a list of section assignment set pairs."""
    for line in problem_input:
        left_section_string, right_section_string = line.rstrip("\n").split(",")
        left_set = assignment_set_from_string(left_section_string)
        right_set = assignment_set_from_string(right_section_string)
        yield left_set, right_set


def solve(problem_input):
    """Solve Advent of Code day 4."""
    fully_overlapping_pairs_count = 0
    overlapping_pairs_count = 0
    for left_set, right_set in parse(problem_input):
        if left_set & right_set:
            overlapping_pairs_count += 1
            if left_set.issubset(right_set) or right_set.issubset(left_set):
                fully_overlapping_pairs_count += 1
    return fully_overlapping_pairs_count, overlapping_pairs_count


part_1_solution, part_2_solution = solve(get_input())
print(part_1_solution)
print(part_2_solution)
