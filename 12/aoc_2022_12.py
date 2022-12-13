"""Advent of Code day 12."""

import string
import heapq


class PriorityQueue:
    """Priority queue class. Mostly copied from https://docs.python.org/3/library/heapq.html."""
    REMOVED = object()

    def __init__(self):
        """Initialize a priority queue."""
        self.pq = []
        self.entries = {}

    def add_item(self, item, priority):
        """Add a new item to the priority queue."""
        entry = [priority, item]
        self.entries[item] = entry
        heapq.heappush(self.pq, entry)

    def del_item(self, item):
        """Delete an item from the priority queue."""
        entry = self.entries.pop(item)
        entry[-1] = self.REMOVED

    def pop(self):
        """Pop the minimum item from the priority queue."""
        while self.pq:
            entry = heapq.heappop(self.pq)
            if entry[-1] is not self.REMOVED:
                del self.entries[entry[-1]]
                return entry
        raise Exception("Queue is empty")


def get_input(name):
    """Read problem input."""
    with open(name, encoding="utf-8") as f:
        return f.readlines()


HEIGHT_MAP = {character: index for index, character in enumerate(string.ascii_lowercase)}


def parse(problem_input):
    """Parse the problem input."""
    # pylint: disable=consider-using-enumerate
    start_node = None
    end_node = None
    problem_input = [list(line.rstrip("\n")) for line in problem_input]
    heights = [[None for _ in line] for line in problem_input]
    for i in range(len(problem_input)):
        for j in range(len(problem_input[0])):
            if problem_input[i][j] == "S":
                start_node = (i, j)
                problem_input[i][j] = "a"
            elif problem_input[i][j] == "E":
                end_node = (i, j)
                problem_input[i][j] = "z"
            heights[i][j] = HEIGHT_MAP[problem_input[i][j]]
    return heights, start_node, end_node


def bounds_check(node, n_rows, n_cols):
    """Check if the given node is within bounds."""
    return node[0] >= 0 and node[1] >= 0 and node[0] < n_rows and node[1] <= n_cols


def neighbours(node, height_map, n_rows, n_cols):
    """Return all neighbour indices within bounds."""
    for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        neighbour = (node[0] + delta[0], node[1] + delta[1])
        if bounds_check(neighbour, n_rows, n_cols):
            current_height = height_map[node[0]][node[1]]
            neighbour_height = height_map[neighbour[0]][neighbour[1]]
            print(f"height: {neighbour_height}")
            if abs(neighbour_height - current_height) <= 1:
                yield neighbour


def shortest_path(height_map, start_node, end_node):
    """Find the shortest length path from start_node to end_node."""
    n_rows = len(height_map)
    n_cols = len(height_map)
    distances= {start_node: 0}
    queue = PriorityQueue()
    queue.add_item(start_node, 0)
    while end_node not in distances:
        print(queue.pq)
        _, next_node = queue.pop()
        neighbour_distance = distances[next_node] + 1
        for neighbour in neighbours(next_node, height_map, n_rows, n_cols):
            if neighbour not in distances or neighbour_distance < distances[neighbour]:
                distances[neighbour] = neighbour_distance
                queue.add_item(neighbour, neighbour_distance)
    return distances[end_node]


def main():
    """Advent of Code day 12 solution."""
    height_map, start, end = parse(get_input("day12_input.txt"))
    print(start, end)
    print(shortest_path(height_map, start, end))


main()
