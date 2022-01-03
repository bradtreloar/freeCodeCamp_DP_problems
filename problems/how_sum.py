# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple
import unittest


def how_sum(target_sum: int, nums: List[int], memo=None) -> Optional[List[int]]:
    if memo is None:
        memo = {}
    if target_sum in memo:
        return None
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    # Return the first solution we find.
    for num in nums:
        remainder = target_sum - num
        solution = how_sum(remainder, nums, memo)
        if solution is not None:
            solution.append(num)
            memo[target_sum] = True
            return solution
    memo[target_sum] = None
    return None


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                (7, [5, 3, 4]),
                [3, 4],
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
            solution = how_sum(*inputs)
            if solution:
                self.assertEqual(sorted(output), sorted(solution))
            else:
                self.assertEqual(output, solution)
