
import sys
from typing import List, Optional, Tuple
import unittest


def grid_traveller(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    table: List[List[int]] = []
    for i in range(m):
        table.append([])
        for j in range(n):
            if i == 0 or j == 0:
                solution = 1
            else:
                solution = table[i][j-1] + table[i-1][j]
            table[i].append(solution)
    return table[m-1][n-1]


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
