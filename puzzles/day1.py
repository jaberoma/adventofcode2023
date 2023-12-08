from shared.common_functions import read_input_file

SPELL_DIGIT_MAP = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}


def solve_problem_a(input_file):
    data = read_input_file(input_file)
    total = 0
    for line in data:
        line_numbers = find_numbers(line)
        number = line_numbers.get_number()
        if number is not None:
            total += number

    return total


def solve_problem_b(input_file):
    data = read_input_file(input_file)
    total = 0
    for line in data:
        line_numbers = find_numbers(line)
        line_numbers = find_spelled_numbers(line, line_numbers)
        number = line_numbers.get_number()
        if number is not None:
            total += number

    return total


def find_numbers(line):
    line_numbers = LineNumbers(None, None, None, None)
    for idx in range(len(line)):
        if line[idx].isdigit():
            line_numbers.update_first(line[idx], idx)

        last_pos_to_check = len(line) - idx - 1
        if line[last_pos_to_check].isdigit():
            line_numbers.update_last(line[last_pos_to_check], last_pos_to_check)

    return line_numbers


def find_spelled_numbers(line, line_numbers):
    texts = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for text in texts:
        position = -1
        while True:
            position = line.find(text, position + 1)
            if position == -1:
                break
            line_numbers.update_first(SPELL_DIGIT_MAP[text], position)
            line_numbers.update_last(SPELL_DIGIT_MAP[text], position)

    return line_numbers


class LineNumbers:
    def __init__(self, first, first_idx, last, last_idx):
        self.first = first
        self.first_idx = first_idx
        self.last = last
        self.last_idx = last_idx

    def update_first(self, new_first, new_first_idx):
        if self.first is None or new_first_idx < self.first_idx:
            self.first = new_first
            self.first_idx = new_first_idx

    def update_last(self, new_last, new_last_idx):
        if self.last is None or new_last_idx > self.last_idx:
            self.last = new_last
            self.last_idx = new_last_idx

    def get_number(self):
        if self.first is not None and self.last is not None:
            return int(str(self.first) + str(self.last))
