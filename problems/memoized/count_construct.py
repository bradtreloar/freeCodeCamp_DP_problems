# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple
import unittest


def count_construct(target_string: str, strings: List[str], memo=None) -> int:
    # Memo.
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    # Base case.
    if len(target_string) == 0:
        return 1
    # Count the number of solutions.
    memo[target_string] = 0
    for string in strings:
        length_is_ok = len(string) <= len(target_string)
        match_at_start = target_string[:len(string)] == string
        if length_is_ok and match_at_start:
            remainder = target_string[len(string):]
            solution = count_construct(remainder, strings, memo)
            if solution > 0:
                memo[target_string] += 1
    return memo[target_string]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                ("abcdef", ["ab", "abc", "cd", "def", "abcd"]),
                1,
            ),
            (
                ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
                0,
            ),
            (
                ("", ["cat", "dog", "mouse"]),
                1,
            ),
            (
                ("purple", ["purp", "p", "ur", "le", "purpl"]),
                2,
            ),
        ]

        for inputs, output in fixtures:
            solution = count_construct(*inputs)
            self.assertEqual(output, solution)
