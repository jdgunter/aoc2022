"""Solution to AOC day 3."""

import string


ITEM_PRIORITIES = {
    ch: index + 1 for index, ch in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


def get_input():
    """Read problem input."""
    with open("day3_input.txt", encoding="utf-8") as f:
        return f.readlines()


def duplicate_item_priority(compartment_1, compartment_2):
    """Compute the rucksack priority according to the priority of the duplicate item."""
    duplicate = compartment_1 & compartment_2
    assert len(duplicate) == 1
    return ITEM_PRIORITIES[min(duplicate)]


def parse_line(line):
    """Parse an input line into the two rucksack compartments."""
    line = line.rstrip("\n")
    halfway = int(len(line)/2)
    compartment_1 = set(line[:halfway])
    compartment_2 = set(line[halfway:])
    return compartment_1, compartment_2


def sum_rucksack_priorities(problem_input, rucksack_priority_fn):
    """Sum the priority of each rucksack according to a given rucksack priority function."""
    priority_sum = 0
    for line in problem_input:
        compartment_1, compartment_2 = parse_line(line)
        priority_sum += rucksack_priority_fn(compartment_1, compartment_2)
    return priority_sum


def sum_elf_group_badge_priorities(problem_input):
    """Sum the priorities of each elf group."""
    priority_sum = 0
    elf_groups = (problem_input[index:index + 3] for index in range(0, len(problem_input), 3))
    for elf_group_strings in elf_groups:
        badge_item = set.intersection(
            *(set(elf_string.rstrip("\n")) for elf_string in elf_group_strings))
        priority_sum += ITEM_PRIORITIES[min(badge_item)]
    return priority_sum


problem_input_strings = get_input()
print(sum_rucksack_priorities(problem_input_strings, duplicate_item_priority))
print(sum_elf_group_badge_priorities(problem_input_strings))
