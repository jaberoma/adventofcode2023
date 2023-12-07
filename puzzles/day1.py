from shared.common_functions import read_input_file


def solve_problem_a():
    data = read_input_file("../input_data/day1_test1.txt")
    total = 0
    for line in data:
        (first, last) = (None, None)
        for idx in range(len(line)):
            if first is None and line[idx].isdigit():
                first = line[idx]

            last_pos_to_check = len(line)-idx-1
            if last is None and line[last_pos_to_check].isdigit():
                last = line[last_pos_to_check]

            if first is not None and last is not None:
                total += int(first + last)
                break

    return total


def solve_problem_b():
    data = read_input_file("../input_data/day1_test2.txt")
    # Implementation for problem B of Day 1
    pass
