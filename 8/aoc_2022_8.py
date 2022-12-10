"""Solution to AOC Day 7."""

from collections import defaultdict


def get_input():
    """Read problem input."""
    with open("day8_input.txt", encoding="utf-8") as f:
        return f.readlines()


def parse(problem_input):
    """Parse problem input into a grid of integers."""
    return [[int(character) for character in row.rstrip("\n")] for row in problem_input]


def transpose(matrix):
    """Transpose a matrix."""
    return [list(c) for c in zip(*matrix)]


def visible_from_left(row, index):
    """Check visibility of the tree in this row at the given index from the left side."""
    tree_height = row[index]
    for i in range(index):
        if row[i] >= tree_height:
            return False
    return True


def visible_from_right(row, index):
    """Check visibility of the tree in this row at the given index from the right side."""
    tree_height = row[index]
    for i in range(index+1, len(row)):
        if row[i] >= tree_height:
            return False
    return True


def horizontally_visible_indices(grid, transposed=False):
    """Count the number of trees visible horizontally."""
    visible_indices = set()
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if visible_from_left(row, j) or visible_from_right(row, j):
                if not transposed:
                    visible_indices.add((i,j))
                else:
                    visible_indices.add((j, i))
    return visible_indices


def left_scenic_score(row, index):
    """Compute the left scenic score, i.e. the number of trees left before the first tree
    at least as high as the tree at the given index."""
    scenic_score = 0
    i = index-1
    while i >= 0:
        scenic_score += 1
        if row[i] >= row[index]:
            break
        i -= 1
    return scenic_score


def right_scenic_score(row, index):
    """Compute the right scenic score, i.e. the number of trees right before the first tree
    at least as high as the tree at the given index."""
    scenic_score = 0
    i = index+1
    while i < len(row): 
        scenic_score += 1
        if row[i] >= row[index]:
            break
        i += 1
    return scenic_score


def horizontal_scenic_scores(grid, scenic_scores=None, transposed=False):
    """Compute the (horizontal) scenic score for each tree in the grid."""
    if scenic_scores is None:
        scenic_scores = defaultdict(lambda: 1)
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            scenic_score = left_scenic_score(row, j) * right_scenic_score(row, j)
            if not transposed:
                scenic_scores[(i,j)] *= scenic_score
            else:
                scenic_scores[(j,i)] *= scenic_score
    return scenic_scores


def all_visible_indices(grid):
    """Return the set of all visible tree indices in the grid."""
    visible_indices = horizontally_visible_indices(grid)
    return visible_indices.union(horizontally_visible_indices(transpose(grid), transposed=True))


def all_scenic_scores(grid):
    """Return a map from all tree indices in the grid to their scenic scores."""
    scenic_scores = horizontal_scenic_scores(grid)
    return horizontal_scenic_scores(transpose(grid), scenic_scores, transposed=True)


EXAMPLE_INPUT = """30373
25512
65332
33549
35390"""


def test():
    """Test solution."""
    trees = parse(EXAMPLE_INPUT.split("\n"))
    count = len(all_visible_indices(trees))
    assert count == 21, count
    max_scenic_score = max(all_scenic_scores(trees).values())
    assert max_scenic_score == 8, max_scenic_score
    print("Tests passed!")


def main():
    """Solve day 8."""
    trees = parse(get_input())
    print(len(all_visible_indices(trees)))
    print(max(all_scenic_scores(trees).values()))


test()
main()
