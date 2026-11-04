# Two Sum

[LeetCode](https://leetcode.com/problems/two-sum/) · Pattern: 01-hashing · Difficulty: E  
Time: O(n) · Space: O(n)

## Question

You get an array `nums` and a number `target`. Return the indices of the two numbers that add up to `target`. There is exactly one answer, and you can't use the same element twice.

Example: `nums = [2, 7, 11, 15], target = 9` → `[0, 1]` (2 + 7 = 9)

## How I solved it

1. Keep a dictionary `seen` that maps a value to the index where I saw it.
2. Walk the array once. For each number `i` at index `idx`, the partner I need is `diff = target - i`.
3. If `diff` is already in `seen`, I found the pair: return `[idx, seen[diff]]`.
4. Otherwise store the current number: `seen[i] = idx`, and move on.

## Key idea

Look up `target - x` **before** storing `x`. That order is what stops a number from pairing with itself (for `[3, 1, 3]`, target 6, it returns `[2, 0]`, not `[0, 0]`). One pass, O(1) per lookup, so O(n).

## Edge cases

- Duplicates: `[3, 3]`, target 6 → `[1, 0]`.
- Negative numbers work the same way.

## My code

```python
from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = defaultdict(int)

        for idx, i in enumerate(nums):
            diff = target - i
            if diff in seen:
                return[idx,seen[diff]]
            seen[i]=idx
```
