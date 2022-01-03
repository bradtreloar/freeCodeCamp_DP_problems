
import sys
from typing import List, Optional, Tuple, cast
import unittest


def best_sum(target_sum: int, nums: List[int]) -> Optional[List[int]]:
    n = target_sum + 1
    table: List[Optional[List[int]]] = [
        [] if i == 0 else None for i in range(n)]
    for i in range(n):
        if table[i] is not None:
            for num in nums:
                sum = i + num
                solution = [*cast(List[int], table[i]), num]
                if sum < n:
                    is_first_solution = table[sum] is None
                    is_best_solution = is_first_solution or len(
                        solution) < len(cast(List[int], table[sum]))
                    if is_best_solution:
                        table[sum] = solution
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
