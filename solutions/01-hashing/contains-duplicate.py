# Contains Duplicate · https://leetcode.com/problems/contains-duplicate/
# Pattern: 01-hashing · Difficulty: E
# Time: O(n) · Space: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums)!=len(set(nums))
