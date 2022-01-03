# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, TypedDict
import unittest


def can_construct(target_string: str, strings: List[str], memo=None) -> bool:
    # Memo
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    # Base case.
    if len(target_string) == 0:
        return True
    # Search for a string that matches the beginning of the target string.
    for string in strings:
        length_is_ok = len(string) <= len(target_string)
        match_at_start = target_string[:len(string)] == string
        if length_is_ok and match_at_start:
            remainder = target_string[len(string):]
            if can_construct(remainder, strings, memo):
                memo[target_string] = True
                return memo[target_string]
    memo[target_string] = False
    return memo[target_string]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                ("abcdef", ["ab", "abc", "cd", "def", "abcd"]),
                True,
            ),
            (
                ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
                False,
            ),
            (
                ("", ["cat", "dog", "mouse"]),
                True,
            ),
        ]

        for inputs, output in fixtures:
            solution = can_construct(*inputs)
            self.assertEqual(output, solution)
