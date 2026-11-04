# Group Anagrams · https://leetcode.com/problems/group-anagrams/
# Pattern: 01-hashing · Difficulty: M
# Time: O(n·k log k) · Space: O(n·k), n = number of strings, k = longest string
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = defaultdict(list)
        ans=[]
        for i in strs:
            curr=tuple(sorted(i))
            seen[curr].append(i)

        for i in seen:
            ans.append(seen.get(i))
        return ans
