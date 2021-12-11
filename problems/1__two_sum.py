# https://leetcode.com/problems/two-sum/description/

from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            j = hashmap.get(diff)
            if j is not None:
                return [i, j]
            hashmap[num] = i


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        fixtures = [
            (
                [2, 7, 11, 15],
                9,
                [0, 1],
            ),
            (
                [3, 2, 4],
                6,
                [1, 2],
            ),
            (
                [3, 3],
                6,
                [0, 1],
            ),
        ]

        for nums, target, expected_result in fixtures:
            result = Solution().twoSum(nums, target)
            self.assertEqual(sorted(expected_result), sorted(result))
