import re
from functools import reduce
from operator import mul

from shared.common_functions import read_input_file

CUBES_CONSTRAINT = {
    'red': 12, 'green': 13, 'blue': 14
}


def solve_problem_a(input_file):
    data = read_input_file(input_file)
    total = 0
    for game in data:
        abort_group = False
        pattern = re.compile(r'Game (\d+):(.*)')
        match = pattern.match(game)
        if match:
            game_number = int(match.group(1))
            sets = match.group(2).split(';')
            for set_of_cubes in sets:
                cubes = set_of_cubes.strip().split(',')
                for cube in cubes:
                    colour_and_number = cube.strip().split()
                    if len(colour_and_number) == 2:
                        count = int(colour_and_number[0])
                        color = colour_and_number[1].lower()
                        if CUBES_CONSTRAINT[color] < count:
                            abort_group = True
                            break

                if abort_group:
                    break

            if not abort_group:
                total += game_number

    return total


def solve_problem_b(input_file):
    data = read_input_file(input_file)
    total = 0
    for game in data:
        pattern = re.compile(r'Game (\d+):(.*)')
        match = pattern.match(game)
        if match:
            sets = match.group(2).split(';')
            minimum_cube_colours = {}
            for set_of_cubes in sets:
                cubes = set_of_cubes.strip().split(',')
                for cube in cubes:
                    colour_and_number = cube.strip().split()
                    if len(colour_and_number) == 2:
                        count = int(colour_and_number[0])
                        color = colour_and_number[1].lower()
                        minimum_cube_colours[color] = max(minimum_cube_colours.get(color, count), count)

            total += reduce(mul, minimum_cube_colours.values(), 1)

    return total
