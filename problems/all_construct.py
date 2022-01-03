# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple
import unittest


def all_construct(target_string: str, strings: List[str], memo=None) -> List[List[str]]:
    # Memo.
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    # Base case.
    if len(target_string) == 0:
        return [[]]
    # Count the number of solutions.
    memo[target_string] = []
    for string in strings:
        length_is_ok = len(string) <= len(target_string)
        match_at_start = target_string[:len(string)] == string
        if length_is_ok and match_at_start:
            remainder = target_string[len(string):]
            solution = all_construct(remainder, strings, memo)
            if len(solution) > 0:
                solution = [[*s, string] for s in solution]
                memo[target_string].extend(solution)
    return memo[target_string]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                ("abcdef", ["ab", "abc", "cd", "def", "abcd"]),
                [["abc", "def"]],
            ),
            (
                ("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]),
                [
                    ["ab", "cd", "ef"],
                    ["abc", "def"],
                    ["ab", "c", "def"],
                    ["abcd", "ef"],
                ],
            ),
            (
                ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
                [],
            ),
            (
                ("", ["cat", "dog", "mouse"]),
                [[]],
            ),
            (
                ("purple", ["purp", "p", "ur", "le", "purpl"]),
                [["purp", "le"], ["p", "ur", "p", "le"]],
            ),
        ]

        def contains(solution, target):
            for s in solution:
                try:
                    self.assertEqual(sorted(s), sorted(target))
                    return True
                except AssertionError:
                    pass
            return False

        for inputs, output in fixtures:
            solution = all_construct(*inputs)
            self.assertEqual(len(output), len(solution))
            for target in output:
                self.assertTrue(contains(solution, target),
                                f"solution does not contain {target}\n\nSolution: {solution}")
