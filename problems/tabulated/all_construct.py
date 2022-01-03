# https://youtu.be/oBt53YbR9Kk?t=4198

import sys
from typing import List, Optional, Tuple, cast
import unittest


def all_construct(target_string: str, strings: List[str]) -> List[List[str]]:
    n = len(target_string) + 1
    table: List[List[List[str]]] = [[] for i in range(n)]
    table[0].append(cast(List[str], []))
    for i in range(n):
        if len(table[i]) > 0:
            for string in strings:
                j = i + len(string)
                if j < n and target_string[i:j] == string:
                    table[j].extend([[*solution, string]
                                     for solution in table[i]])
    return table[len(target_string)]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        sys.setrecursionlimit(10000)

        fixtures = [
            (
                ("", ["cat", "dog", "mouse"]),
                [[]],
            ),
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
                ("purple", ["purp", "p", "ur", "le", "purpl"]),
                [["purp", "le"], ["p", "ur", "p", "le"]],
            ),
        ]

        def contains(solution, target):
            for s in solution:
                try:
                    self.assertEqual(s, target)
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
