"""Advent of Code day 11."""

from dataclasses import dataclass
from functools import reduce


def get_input(name):
    """Read problem input."""
    with open(name, encoding="utf-8") as f:
        return f.readlines()


@dataclass
class Monkey:
    """Simple dataclass representing a monkey."""
    items: list[int]
    operation: callable
    test: int
    on_true: int
    on_false: int
    num_inspections: int = 0


def parse_monkey(monkey_lines):
    """Parse a single monkey object."""
    # pylint: disable=eval-used,unnecessary-lambda-assignment,redefined-outer-name
    items = [int(num_string.strip()) for num_string in monkey_lines[1].strip(" \n")[15:].split(",")]
    operation = lambda old: eval(monkey_lines[2].strip(" \n")[16:])
    test = int(monkey_lines[3].rstrip().split()[-1])
    on_true = int(monkey_lines[4].rstrip().split()[-1])
    on_false = int(monkey_lines[5].rstrip().split()[-1])
    return Monkey(items, operation, test, on_true, on_false)



def parse_monkeys(problem_input):
    """Parse all monkeys in the problem input."""
    chunks = [problem_input[index:index+6] for index in range(0, len(problem_input), 7)]
    return [parse_monkey(chunk) for chunk in chunks]


def _gcd(a, b):
    """Compute the greatest common divisor of a pair of integers.
    Taken from https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations."""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def gcd(*args):
    """Compute the greatest common divisor of a list of integers."""
    assert len(args) >= 2
    result = _gcd(args[0], args[1])
    for arg in args[3:]:
        result = _gcd(result, arg)
    return result


def lcm(*args):
    """Find the lowest common multiple of a list of integers."""
    return int(reduce(lambda x, y: x*y, args)/gcd(*args))


def evaluate_round(monkeys, divide_worry_levels=True):
    """Evaluate a round of monkeys throwing objects.
    Returns a new list of monkeys with updated state."""
    # Perform all worry level computations modulo the lcm(monkey test divisors) in
    # order to keep worry level sizes relatively small.
    N = lcm(*(monkey.test for monkey in monkeys))  # pylint: disable=invalid-name
    for monkey in monkeys:
        for worry_level in monkey.items:
            monkey.num_inspections += 1
            worry_level = monkey.operation(worry_level)
            if divide_worry_levels:
                worry_level //= 3
            worry_level = worry_level % N
            if worry_level % monkey.test == 0:
                monkeys[monkey.on_true].items.append(worry_level)
            else:
                monkeys[monkey.on_false].items.append(worry_level)
        monkey.items = []
    return monkeys


def monkey_business(monkeys):
    """Compute the level of monkey business performed by the given monkeys."""
    most_active_monkeys = list(sorted(monkeys, key=lambda m: m.num_inspections))[-2:]
    return most_active_monkeys[0].num_inspections * most_active_monkeys[1].num_inspections


def test():
    """Test solution."""
    monkeys = parse_monkeys(get_input("test_input.txt"))
    for _ in range(20):
        monkeys = evaluate_round(monkeys)
    assert monkey_business(monkeys) == 10605, monkeys
    monkeys = parse_monkeys(get_input("test_input.txt"))
    for _ in range(10000):
        monkeys = evaluate_round(monkeys, divide_worry_levels=False)
    assert monkey_business(monkeys) == 2713310158, monkeys
    print("Tests passed!")


def main():
    """Solve Advent of Code day 11."""
    # Part 1.
    monkeys = parse_monkeys(get_input("day11_input.txt"))
    for _ in range(20):
        monkeys = evaluate_round(monkeys)
    print(monkey_business(monkeys))
    # Part 2. Just re-parse the input instead of making a copy of the initial state.
    monkeys = parse_monkeys(get_input("day11_input.txt"))
    for _ in range(10000):
        monkeys = evaluate_round(monkeys, divide_worry_levels=False)
    print(monkey_business(monkeys))


test()
main()
