# Concatenation of Array

[LeetCode](https://leetcode.com/problems/concatenation-of-array/) · Pattern: 00-basics · Difficulty: E  
Time: O(n) · Space: O(n)

## Question

You get an array `nums` of length n. Return a new array of length 2n that is `nums` followed by `nums` again.

Example: `nums = [1, 2, 1]` → `[1, 2, 1, 1, 2, 1]`

## How I solved it

1. The answer is just the array written twice, one copy after the other.
2. In Python, `+` on two lists joins them into a new list, so `nums + nums` is the whole answer.

## Key idea

`ans[i] = nums[i]` and `ans[i + n] = nums[i]`, which is the same as joining the list to itself.

## Edge cases

- One element: `[5]` → `[5, 5]`.

## My code

```python
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```
