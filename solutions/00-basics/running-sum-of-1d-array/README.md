# Running Sum of 1d Array

[LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) · Pattern: 00-basics · Difficulty: E  
Time: O(n) · Space: O(n)

## Question

You get an array `nums`. Return an array where position i holds the sum of `nums[0]` up to `nums[i]`.

Example: `nums = [1, 2, 3, 4]` → `[1, 3, 6, 10]`

## How I solved it

1. Keep one running total `rs`, starting at 0.
2. Walk the array once. For each number, add it to `rs`.
3. After adding, append `rs` to the answer. That value is the sum of everything up to here.

## Key idea

Each running sum is the previous running sum plus the current number, so you never re-add from the start. One pass, O(n).

## Edge cases

- Negative numbers work the same way.
- One element: the answer is that element.

## My code

```python
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans=[]
        rs=0
        for i in nums:
            rs+=i
            ans.append(rs)
        return ans
```
