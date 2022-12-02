"""Solution to AOC Day 1."""

import heapq


def get_input():
    """Read problem input."""
    with open("day1_input.txt", encoding="utf-8") as f:
        return f.readlines()


def parse(problem_input):
    """Parse the problem input into a list of lists.
    
    Each sublist contains the items carried by the elf at that sublist index.
    """
    elf_items = []
    current_elf_items = []
    for line in problem_input:
        line = line.rstrip("\n")
        if line == "":
            elf_items.append(current_elf_items)
            current_elf_items = []
        else:
            current_elf_items.append(int(line))
    return elf_items


def find_max_calories(elf_items, num_max):
    """Find the sum of calories carried by the num_max elves with the highest load."""
    max_calories = []
    for current_elf_items in elf_items:
        current_sum = sum(current_elf_items)
        if len(max_calories) < num_max:
            heapq.heappush(max_calories, current_sum)
        else:
            heapq.heappushpop(max_calories, current_sum)
    return sum(max_calories)


parsed_input = parse(get_input())
print(find_max_calories(parsed_input, num_max=1))
print(find_max_calories(parsed_input, num_max=3))
