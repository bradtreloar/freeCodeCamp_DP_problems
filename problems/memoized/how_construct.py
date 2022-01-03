
import sys
from typing import List, Optional, Tuple
import unittest


def how_construct(target_string: str, strings: List[str], memo=None) -> Optional[List[str]]:
    # Memo.
    if memo is None:
        memo = {}
    if target_string in memo:
        return memo[target_string]
    # Base case.
    if len(target_string) == 0:
        return []
    # Return the first solution we find.
    for string in strings:
        length_is_ok = len(string) <= len(target_string)
        match_at_start = target_string[:len(string)] == string
        if length_is_ok and match_at_start:
            remainder = target_string[len(string):]
            solution = how_construct(remainder, strings, memo)
            if solution is not None:
                solution.append(string)
                memo[target_string] = solution
                return memo[target_string]
    memo[target_string] = None
    return memo[target_string]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                ("abcdef", ["ab", "abc", "cd", "def", "abcd"]),
                ["abc", "def"],
            ),
            (
                ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
                None,
            ),
            (
                ("", ["cat", "dog", "mouse"]),
                [],
            ),
        ]

        for inputs, output in fixtures:
            solution = how_construct(*inputs)
            if solution:
                self.assertEqual(sorted(output), sorted(solution))
            else:
                self.assertEqual(output, solution)
