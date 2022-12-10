"""Advent of Code day 10."""


class CPUState:
    """Manage the current CPU state."""

    def __init__(self):
        """Initialize a CPUState object."""
        self.cycle = 1
        self.x = 1
        self.interesting_cycles = (20, 60, 100, 140, 180, 220)
        self.signal_strength_sum = 0
        self.image = [[" " for _ in range(40)] for _ in range(6)]

    def increment_cycle(self):
        "Increment the cycle."
        if self.cycle in self.interesting_cycles:
            self.signal_strength_sum += self.cycle * self.x
        pixel_row = (self.cycle - 1) // 40
        pixel_position = (self.cycle - 1) % 40
        if pixel_position in (self.x - 1, self.x, self.x + 1):
            self.image[pixel_row][pixel_position] = "#"
        else:
            self.image[pixel_row][pixel_position] = "."
        self.cycle += 1

    def addX(self, value):
        """Add a value to the X register."""
        self.x += value

    def image_string(self):
        """Get the image string generated during execution."""
        lines = []
        for line in self.image:
            lines.append("".join(line) + "\n")
        return "".join(lines)


def get_input(name):
    """Read problem input."""
    with open(name, encoding="utf-8") as f:
        return f.readlines()


def parse_intructions(problem_input):
    """Parse instructions from the problem input."""
    instructions = []
    for instruction in problem_input:
        instruction = instruction.rstrip("\n")
        if instruction.startswith("addx"):
            instruction = int(instruction.split(" ")[1])
        instructions.append(instruction)
    return instructions


def execute(instructions):
    """Execute the given instructions. Returns the sum of interesting signal strengths."""
    cpu = CPUState()
    for instruction in instructions:
        if instruction == "noop":
            cpu.increment_cycle()
        else:
            cpu.increment_cycle()
            cpu.increment_cycle()
            cpu.addX(instruction)
    return cpu


EXAMPLE_IMAGE = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""


def test():
    """Test day 10 solution."""
    cpu = execute(parse_intructions(get_input("test_input.txt")))
    assert cpu.signal_strength_sum == 13140, cpu.signal_strength_sum
    assert cpu.image_string() == EXAMPLE_IMAGE, cpu.image_string()
    print("Tests passed!")


def main():
    """Advent of Code day 10."""
    cpu = execute(parse_intructions(get_input("day10_input.txt")))
    print(cpu.signal_strength_sum)
    print(cpu.image_string())


test()
main()
