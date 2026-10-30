# Concatenation of Array · https://leetcode.com/problems/concatenation-of-array/
# Pattern: 00-basics · Difficulty: E
# Time: O(n) · Space: O(n)
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
