"""Solution to AOC Day 7."""

def get_input():
    """Read problem input."""
    with open("day8_input.txt", encoding="utf-8") as f:
        return f.readlines()


def parse(problem_input):
    """Parse problem input into a grid of integers."""
    return [[int(character) for character in row.rstrip("\n")] for row in problem_input]


def check_visibility_from_top(grid):
    """Count the number of trees visible from the top edge."""
    visible = [[1 for _ in grid[0]]] + [[0 for _ in row] for row in grid[1:]]
    for row_index, row in enumerate(grid):
        if row_index == 0:
            continue
        any_visible = False
        for column_index, tree_height in enumerate(row):
            if not bool(visible[row_index-1][column_index]):
                visible[row_index][column_index] = 0
            else:
                is_visible = 1 if tree_height >= grid[row_index-1][column_index] else 0
                any_visible = any_visible or bool(is_visible)
                visible[row_index][column_index] = is_visible
        if not any_visible:
            return visible
    return visible
