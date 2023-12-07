import unittest
from puzzles.day1 import solve_problem_a, solve_problem_b


class TestDay1(unittest.TestCase):
    def test_solve_problem_a(self):
        result = solve_problem_a()
        expected_result = 54644
        self.assertEqual(expected_result, result)

    def test_solve_problem_b(self):
        result = solve_problem_b()
        # Add assertions to test the result


if __name__ == '__main__':
    unittest.main()
