# Group Anagrams

[LeetCode](https://leetcode.com/problems/group-anagrams/) · Pattern: 01-hashing · Difficulty: M  
Time: O(n·k log k) · Space: O(n·k), n = number of strings, k = longest string

## Question

You get a list of strings `strs`. Group the words that are anagrams of each other (same letters, same counts, any order). Return the groups in any order.

Example: `["eat", "tea", "tan", "ate", "nat", "bat"]` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

## How I solved it

1. Anagrams have the same letters, so if I sort each word's letters they become identical: `"eat"`, `"tea"`, `"ate"` all sort to `a, e, t`.
2. Use that sorted form as a dictionary key. A list can't be a dict key, so I turn it into a tuple: `tuple(sorted(word))`.
3. Use a `defaultdict(list)`: for each word, append it to the list under its key.
4. At the end, every value in the dictionary is one group. Return all the values.

## Key idea

Key = `tuple(sorted(word))`, value = list of words with that key. Sorting each word costs O(k log k), so total O(n·k log k).

## Edge cases

- Empty string `""` is its own group: `[[""]]`.
- A single word → one group with that word.

## My code

```python
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
```
