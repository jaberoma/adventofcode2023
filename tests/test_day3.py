import unittest

from parameterized import parameterized

from puzzles.day3 import solve_problem_a, solve_problem_b


class TestDay3(unittest.TestCase):
    @parameterized.expand([
        ("../input_data/day3_sample.txt", 4361),
        ("../input_data/day3.txt", 522726),
    ])
    def test_solve_problem_a(self, input_file, expected_result):
        result = solve_problem_a(input_file)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ("../input_data/day3_sample.txt", 467835),
        ("../input_data/day3.txt", 81721933),
    ])
    def test_solve_problem_b(self, input_file, expected_result):
        result = solve_problem_b(input_file)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
