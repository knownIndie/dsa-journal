# Running Sum of 1d Array · https://leetcode.com/problems/running-sum-of-1d-array/
# Pattern: 00-basics · Difficulty: E
# Time: O(n) · Space: O(n)
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans=[]
        rs=0
        for i in nums:
            rs+=i
            ans.append(rs)
        return ans
