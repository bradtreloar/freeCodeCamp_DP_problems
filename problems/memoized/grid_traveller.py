
import sys
from typing import List, Optional, Tuple
import unittest


def grid_traveller(rows: int, columns: int, memo=None) -> int:
    if memo is None:
        memo = {}
    m, n = (rows, columns) if rows <= columns else (columns, rows)
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    memo[key] = grid_traveller(m, n-1) + grid_traveller(m-1, n)
    return memo[key]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            ((0, 0), 0),
            ((0, 1), 0),
            ((1, 1), 1),
            ((2, 2), 2),
            ((3, 3), 6),
            ((4, 2), 4),
            ((4, 3), 10),
            ((4, 4), 20),
        ]

        for inputs, output in fixtures:
            self.assertEqual(output, grid_traveller(*inputs))
