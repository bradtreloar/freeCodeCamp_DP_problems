# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple
import unittest


def best_construct(target_string: str, strings: List[str], memo=None) -> Optional[List[str]]:
    # Memo.
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    # Base case.
    if len(target_string) == 0:
        return []
    # Keep one of the equal shortest solutions.
    memo[target_string] = None
    for string in strings:
        length_is_ok = len(string) <= len(target_string)
        match_at_start = target_string[:len(string)] == string
        if length_is_ok and match_at_start:
            remainder = target_string[len(string):]
            solution = best_construct(remainder, strings, memo)
            if solution is not None:
                if memo[target_string] is None or len(solution) < len(memo[target_string]):
                    memo[target_string] = solution
    return memo[target_string]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                (7, [5, 3, 4]),
                [3, 4],
            ),
        ]

        for inputs, output in fixtures:
            solution = best_construct(*inputs)
            if solution is not None:
                self.assertEqual(sorted(output), sorted(solution))
            else:
                self.assertEqual(output, solution)
