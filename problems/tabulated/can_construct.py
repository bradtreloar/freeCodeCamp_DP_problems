# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, TypedDict
import unittest


def can_construct(target_string: str, strings: List[str]) -> bool:
    n = len(target_string) + 1
    table = [i == 0 for i in range(n)]
    for i in range(n):
        if table[i]:
            for string in strings:
                j = i + len(string)
                if j < n and target_string[i:j] == string:
                    table[j] = True
    return table[len(target_string)]


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
            (
                ("enterapotentpot", [
                 "a", "p", "ent", "enter", "ot", "o", "t"]),
                True,
            ),
            (
                ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", [
                 "e", "ee", "eee", "eeee", "eeeee", "eeeeee"]),
                True,
            ),
        ]

        for inputs, output in fixtures:
            solution = can_construct(*inputs)
            self.assertEqual(output, solution)
