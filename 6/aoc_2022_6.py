"""Solution to AOC Day 6."""

def get_input():
    """Read problem input."""
    with open("day6_input.txt", encoding="utf-8") as f:
        return f.read()


def find_index_after_start(packet, num_different):
    """Find the index of the start marker, given its length."""
    window_start_index = 0
    window_end_index = num_different
    while window_end_index < len(packet):
        window = packet[window_start_index:window_end_index]
        if len(window) == len(set(window)):
            return window_end_index
        window_start_index += 1
        window_end_index += 1
    raise Exception("No start marker found in packet.")


def test():
    """Test solution."""
    cases = [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 4),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6, 4),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 4),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 4),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19, 14),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23, 14),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23, 14),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29, 14),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26, 14),
    ]
    for test_string, expected, num_different in cases:
        index = find_index_after_start(test_string, num_different)
        assert index == expected, f"Expected: {expected}, Actual: {index}"
    print("All tests passed!")


test()
problem_input = get_input()
print(find_index_after_start(problem_input, num_different=4))
print(find_index_after_start(problem_input, num_different=14))
