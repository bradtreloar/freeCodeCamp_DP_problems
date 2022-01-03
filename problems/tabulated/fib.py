# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple
import unittest


def fib(n: int, table=None) -> int:
    table = []
    for i in range(n + 1):
        if i < 2:
            table.append(i)
        else:
            result = table[i-1] + table[i-2]
            table.append(result)
    return table[n]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (50, 12586269025),
        ]

        for input, output in fixtures:
            self.assertEqual(output, fib(input))
