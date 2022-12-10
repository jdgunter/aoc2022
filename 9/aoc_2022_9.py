"""Advent of code day 9."""

from collections import namedtuple

class Position(namedtuple("Position", ["x", "y"])):
    """Basic position class with an x and y coordinate."""

    def add(self, pos):
        """Add another position to this one and return the result."""
        return Position(self.x + pos.x, self.y + pos.y)

    def difference(self, pos):
        """Compute the difference between two positions."""
        return Position(self.x - pos.x, self.y - pos.y)

    def add_x(self, x):
        """Create a new position with a shifted x coordinate."""
        return Position(self.x + x, self.y)

    def add_y(self, y):
        """Create a new position with a shifted y coordinate."""
        return Position(self.x, self.y + y)


def get_input():
    """Read problem input."""
    with open("day9_input.txt", encoding="utf-8") as f:
        return f.readlines()


DIRECTIONS_MAP = {
    "U": Position(0, 1),
    "D": Position(0, -1),
    "R": Position(1, 0),
    "L": Position(-1, 0),
}


def parse_moves(problem_input):
    """Parse the moves in the problem input."""
    moves = []
    for move in problem_input:
        move = move.rstrip("\n")
        direction, steps = move.split(" ")
        moves.append((DIRECTIONS_MAP[direction], int(steps)))
    return moves


def clamp(val, min, max):
    """Clamp a value to be within the range [min, max]."""
    if val < min:
        return min
    if val > max:
        return max
    return val


def move_tail(tail, head):
    """Move the tail position to follow the head."""
    difference = head.difference(tail)
    if abs(difference.x) <= 1 and abs(difference.y) <= 1:
        return tail
    if difference.x == 0:
        return tail.add_y(clamp(difference.y, -1, 1))
    if difference.y == 0:
        return tail.add_x(clamp(difference.x, -1, 1))
    return tail.add(Position(clamp(difference.x, -1, 1), clamp(difference.y, -1, 1)))


def process_moves(moves, rope_length=2):
    """Process the list of moves. Returns a set of all indices the tail visited."""
    knot_indices = list(range(rope_length))
    knots = [Position(0, 0) for _ in knot_indices]
    visited = {knots[-1]}
    for direction, steps in moves:
        for _ in range(steps):
            knots[0] = knots[0].add(direction)
            for head_index, tail_index in zip(knot_indices, knot_indices[1:]):
                knots[tail_index] = move_tail(knots[tail_index], knots[head_index])
            visited.add(knots[-1])
    return visited


EXAMPLE_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

LARGER_EXAMPLE_INPUT = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def test():
    """Test the solution."""
    moves = parse_moves(EXAMPLE_INPUT.split("\n"))
    visited = process_moves(moves)
    num_visited = len(visited)
    assert num_visited == 13, sorted(visited)
    moves = parse_moves(LARGER_EXAMPLE_INPUT.split("\n"))
    visited = process_moves(moves, rope_length=10)
    num_visited = len(visited)
    assert num_visited == 36, sorted(visited)
    print("Tests passed!")


def main():
    """Advent of Code day 9 solution."""
    moves = parse_moves(get_input())
    print(len(process_moves(moves)))
    print(len(process_moves(moves, rope_length=10)))


test()
main()
