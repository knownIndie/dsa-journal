# Two Sum · https://leetcode.com/problems/two-sum/
# Pattern: 01-hashing · Difficulty: E
# Time: O(n) · Space: O(n)
from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = defaultdict(int)

        for idx, i in enumerate(nums):
            diff = target - i
            if diff in seen:
                return[idx,seen[diff]]
            seen[i]=idx
