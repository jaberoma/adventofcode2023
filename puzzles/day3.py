from shared.common_functions import read_input_file
from collections import defaultdict


def solve_problem_a(input_file):
    data = read_input_file(input_file)
    adjacent_numbers = get_adjacent_numbers(data)
    return sum(adjacent_numbers)


def get_adjacent_numbers(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    adjacent_numbers = []

    for row in range(rows):
        number = None
        for column in range(columns):
            if matrix[row][column].isdigit():
                if number is not None:
                    number = int(str(number) + matrix[row][column])
                else:
                    number = int(matrix[row][column])
                continue
            else:
                if number is not None:
                    if is_adjacent_to_symbol(matrix, rows, columns, row, column, number):
                        adjacent_numbers.append(number)

                    number = None

        if number is not None and is_adjacent_to_symbol(matrix, rows, columns, row, columns, number):
            adjacent_numbers.append(number)

    return adjacent_numbers


def is_adjacent_to_symbol(matrix, rows, columns, row, column, number):
    start_pos = column - len(str(number)) - 1 if column - len(str(number)) - 1 > 0 else 0
    end_pos = column if column < columns else columns - 1
    upper_row = row - 1 if row - 1 >= 0 else 0
    lower_row = row + 1
    if (is_symbol(matrix[row][start_pos])) or is_symbol(matrix[row][end_pos]):
        return True
    elif upper_row >= 0 and any(is_symbol(char) for char in matrix[upper_row][start_pos:end_pos + 1]):
        return True
    elif lower_row < rows and any(is_symbol(char) for char in matrix[lower_row][start_pos:end_pos + 1]):
        return True
    else:
        return False


def is_symbol(character):
    return not character.isdigit() and character is not '.'


def solve_problem_b(input_file):
    data = read_input_file(input_file)
    gear_ratios = get_gear_ratios(data)
    return sum(gear_ratios)


def get_gear_ratios(matrix):
    numbers_and_gears = get_numbers_and_gears(matrix)
    gear_ratios = look_for_gear_ratios(numbers_and_gears)
    return gear_ratios


def get_numbers_and_gears(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    numbers_and_gears = defaultdict(list)
    for row in range(rows):
        number = None
        for column in range(columns):
            if matrix[row][column].isdigit():
                if number is not None:
                    number = int(str(number) + matrix[row][column])
                else:
                    number = int(matrix[row][column])
                continue
            else:
                if number is not None:
                    numbers_and_gears['numbers'].append(Number(number, column - len(str(number)), column - 1, row, columns))
                    number = None

            if matrix[row][column] is '*':
                numbers_and_gears['gears'].append(Gear(column, column, row))

        if number is not None:
            numbers_and_gears['numbers'].append(Number(number, columns - len(str(number)), columns-1, row, columns))

    return numbers_and_gears


def look_for_gear_ratios(numbers_and_gears):
    gears_ratios = []
    for gear in numbers_and_gears["gears"]:
        adjacents = []
        for number in numbers_and_gears["numbers"]:
            if is_gear_adjacent(gear, number):
                adjacents.append(number)

        if len(adjacents) is 2:
            gears_ratios.append(adjacents[0].number * adjacents[1].number)
    return gears_ratios


def is_gear_adjacent(gear, number):
    row, col = gear.position()
    ul_row, ul_col = number.upper_left()
    br_row, br_col = number.bottom_right()

    return ul_row <= row <= br_row and ul_col <= col <= br_col


class Number:
    def __init__(self, number, start_pos, end_pos, row, columns):
        self.number = number
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.row = row
        self.columns = columns

    def upper_left(self):
        start_pos = self.start_pos - 1 if self.start_pos - 1 > 0 else 0
        upper_row = self.row - 1 if self.row - 1 >= 0 else 0
        return start_pos, upper_row

    def bottom_right(self):
        end_pos = self.end_pos + 1 if self.end_pos + 1 < self.columns else self.columns - 1
        lower_row = self.row + 1
        return end_pos, lower_row


class Gear:
    def __init__(self, start_pos, end_pos, row):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.row = row

    def position(self):
        return self.start_pos, self.row
