# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple, cast
import unittest


def count_construct(target_string: str, strings: List[str]) -> int:
    n = len(target_string) + 1
    table: List[int] = [1 if i == 0 else 0 for i in range(n)]
    for i in range(n):
        if table[i] > 0:
            for string in strings:
                j = i + len(string)
                if j < n and target_string[i: j] == string:
                    table[j] += table[i]
    return table[len(target_string)]


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
