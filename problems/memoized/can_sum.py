
import sys
from typing import List, TypedDict
import unittest


def can_sum(target_sum: int, nums: List[int], memo=None) -> bool:
    if memo is None:
        memo = {}
    if target_sum in memo:
        return False
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in nums:
        diff = target_sum - num
        if can_sum(diff, nums, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                (7, [5, 3, 4, 7]),
                True,
            ),
            (
                (7, [2, 4]),
                False,
            ),
            (
                (101, [2, 4, 8, 16, 32, 64]),
                False,
            ),
            (
                (1001, [2, 4, 8, 16, 32, 64]),
                False,
            ),
            (
                (10001, [2, 4, 8, 16, 32, 64]),
                False,
            ),
        ]

        for inputs, output in fixtures:
            solution = can_sum(*inputs)
            self.assertEqual(output, solution)
