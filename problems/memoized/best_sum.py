
import sys
from typing import List, Optional, Tuple
import unittest


def best_sum(target_sum: int, nums: List[int], memo=None) -> Optional[List[int]]:
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    # Select one of the equal shortest solutions.
    memo[target_sum] = None
    for num in nums:
        remainder = target_sum - num
        solution = best_sum(remainder, nums, memo)
        if solution is not None:
            no_prev_solutions = memo[target_sum] is None
            is_better_solution = no_prev_solutions or len(
                solution) < len(memo[target_sum])
            if is_better_solution:
                memo[target_sum] = [num, *solution]
    return memo[target_sum]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                (7, [5, 3, 4]),
                [3, 4],
            ),
            (
                (7, [7, 5, 3, 4]),
                [7],
            ),
            (
                (7, [2, 4]),
                None,
            ),
            (
                (300, [7, 14]),
                None,
            ),
            (
                (0, [1, 2, 3]),
                [],
            ),
        ]

        for inputs, output in fixtures:
            solution = best_sum(*inputs)
            if solution is not None:
                self.assertEqual(sorted(output), sorted(solution))
            else:
                self.assertEqual(output, solution)
