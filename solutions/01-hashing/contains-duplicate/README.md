# Contains Duplicate

[LeetCode](https://leetcode.com/problems/contains-duplicate/) · Pattern: 01-hashing · Difficulty: E  
Time: O(n) · Space: O(n)

## Question

You get an array `nums`. Return `True` if any value appears at least twice, and `False` if every value is distinct.

Example: `[1, 2, 3, 1]` → `True` · `[1, 2, 3, 4]` → `False`

## How I solved it

1. Turn the list into a set. A set keeps only one copy of each value.
2. If there was a repeat, the set is smaller than the list.
3. So the answer is `len(nums) != len(set(nums))`.

## Key idea

"Any repeat?" means "is the set smaller than the list?". Building the set is O(n) time and O(n) space.

## Edge cases

- One element → `False`.
- All the same value → `True`.

## My code

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums)!=len(set(nums))
```
