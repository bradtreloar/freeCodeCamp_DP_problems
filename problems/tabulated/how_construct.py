
import sys
from typing import List, Optional, Tuple, cast
import unittest


def how_construct(target_string: str, strings: List[str]) -> Optional[List[str]]:
    n = len(target_string) + 1
    table: List[Optional[List[str]]] = [
        [] if i == 0 else None for i in range(n)]
    for i in range(n):
        if table[i] is not None:
            for string in strings:
                j = i + len(string)
                if j < n and target_string[i: j] == string:
                    table[j] = [*cast(List[str], table[i]), string]
    return table[len(target_string)]


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
