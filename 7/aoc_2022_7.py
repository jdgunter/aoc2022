"""Solution to AOC Day 7."""

def get_input():
    """Read problem input."""
    with open("day7_input.txt", encoding="utf-8") as f:
        return f.readlines()


class TreeNode:
    """Represents a single node in a tree."""

    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.files = []
        self.size = None

    def add_child(self, child):
        """Add a new child node to this node."""
        self.children.append(child)

    def add_file(self, file_size):
        """Add a new raw data file to this node."""
        self.files.append(file_size)

    def is_root(self):
        """Check if this node is the root node."""
        return self.parent is None

    def compute_size(self):
        """Compute the size and store it on the node.
        Assumes that all the children have already computed their own size."""
        self.size = sum(self.files) + sum(child.size for child in self.children)

    def iterate(self):
        """Iterate over all nodes in the tree."""
        yield self
        for child in self.children:
            for node in child.iterate():
                yield node


def get_listed(remaining_lines):
    """Get the listed children of the current directory."""
    listed = []
    for index, line in enumerate(remaining_lines):
        if line[0] == "$":
            return listed, remaining_lines[index:]
        file_type = line.rstrip("\n").split(" ")[0]
        if file_type == "dir":
            listed.append("dir")
        else:
            listed.append(int(file_type))
    return listed, []


def _build_tree(current_tree, remaining_lines):
    """Add new nodes to the tree based on the remaining lines."""
    if remaining_lines == []:
        current_tree.compute_size()
        if current_tree.is_root():
            return current_tree
        return _build_tree(current_tree.parent, [])
    next_command = remaining_lines[0].rstrip("\n")
    # Handle when the next command lists off child files and directory.
    if next_command == "$ ls":
        listed, remaining_lines = get_listed(remaining_lines[1:])
        for file in listed:
            if isinstance(file, int):
                current_tree.add_file(file)
        return _build_tree(current_tree, remaining_lines)
    # Handle when the next command enters either the parent or a child directory.
    move_to = next_command.split(" ")[-1]
    if move_to == "..":
        current_tree.compute_size()
        return _build_tree(current_tree.parent, remaining_lines[1:])
    new_child = TreeNode(parent=current_tree)
    current_tree.add_child(new_child)
    return _build_tree(new_child, remaining_lines[1:])


def build_tree(lines):
    """Build a tree representing the file directory structure."""
    return _build_tree(TreeNode(None), lines[1:])


def sum_directory_sizes(directory_tree, max_size=100000):
    """Find the sum of directory sizes whose size is less than the given max."""
    return sum(dir.size if dir.size <= max_size else 0 for dir in directory_tree.iterate())


def find_minimum_size_to_delete(directory_tree, min_size=30_000_000, total_size=70_000_000):
    """Find the size of the smallest directory that needs to be deleted to free up space."""
    free_space = total_size - directory_tree.size
    return min(dir.size for dir in directory_tree.iterate() if dir.size >= min_size - free_space)


EXAMPLE_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test():
    """Run tests."""
    lines = EXAMPLE_INPUT.split("\n")
    example_tree = build_tree(lines)
    part1 = sum_directory_sizes(example_tree)
    assert part1 == 95437, part1
    part2 = find_minimum_size_to_delete(example_tree)
    assert part2 == 24933642, part2
    print("Tests passed!")


test()
problem_input = get_input()
tree = build_tree(problem_input)
print(sum_directory_sizes(tree))
print(find_minimum_size_to_delete(tree))
