import unittest

from parameterized import parameterized

from puzzles.day2 import solve_problem_a, solve_problem_b


class TestDay2(unittest.TestCase):
    @parameterized.expand([
        ("../input_data/day2_test1_sample.txt", 8),
        ("../input_data/day2_test1.txt", 2278),
        # Add more test cases as needed
    ])
    def test_solve_problem_a(self, input_file, expected_result):
        result = solve_problem_a(input_file)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ("../input_data/day2_test2_sample.txt", 2286),
        ("../input_data/day2_test2.txt", 67953),
        # Add more test cases as needed
    ])
    def test_solve_problem_b(self, input_file, expected_result):
        result = solve_problem_b(input_file)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
