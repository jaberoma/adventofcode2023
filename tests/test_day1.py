import unittest

from parameterized import parameterized

from puzzles.day1 import solve_problem_a, solve_problem_b


class TestDay1(unittest.TestCase):
    @parameterized.expand([
        ("../input_data/day1_test1_sample.txt", 142),
        ("../input_data/day1_test1.txt", 54644),
        # Add more test cases as needed
    ])
    def test_solve_problem_a(self, input_file, expected_result):
        result = solve_problem_a(input_file)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ("../input_data/day1_test2_sample.txt", 281),
        ("../input_data/day1_test2.txt", 53348),
        # Add more test cases as needed
    ])
    def test_solve_problem_b(self, input_file, expected_result):
        result = solve_problem_b(input_file)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
