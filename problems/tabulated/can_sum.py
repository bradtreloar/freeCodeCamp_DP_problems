
import sys
from typing import List, TypedDict
import unittest


def can_sum(target_sum: int, nums: List[int]) -> bool:
    n = target_sum + 1
    table = [i == 0 for i in range(n)]
    for i in range(n):
        if table[i]:
            for num in nums:
                if i + num < n:
                    table[i + num] = True
    print(table)
    return table[target_sum]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                (7, [7]),
                True,
            ),
            (
                (7, [5, 3, 4]),
                True,
            ),
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
