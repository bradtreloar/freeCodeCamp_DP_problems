
import sys
from typing import cast, List, Optional, Tuple
import unittest


def how_sum(target_sum: int, nums: List[int]) -> Optional[List[int]]:
    n = target_sum + 1
    table: List[Optional[List[int]]] = [
        [] if i == 0 else None for i in range(n)]
    for i in range(n):
        if table[i] is not None:
            for num in nums:
                sum = i + num
                if sum < n:
                    if table[sum] is None:
                        table[sum] = []
                    cast(List[int], table[sum]).append(num)
    return table[target_sum]


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
