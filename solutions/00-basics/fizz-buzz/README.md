# FizzBuzz

[LeetCode](https://leetcode.com/problems/fizz-buzz/) · Pattern: 00-basics · Difficulty: E  
Time: O(n) · Space: O(n)

## Question

Given n, return a list of strings for 1 to n. For each number i:
- divisible by 3 and 5 → `"FizzBuzz"`
- divisible by 3 only → `"Fizz"`
- divisible by 5 only → `"Buzz"`
- otherwise → the number as a string

Example: `n = 5` → `["1", "2", "Fizz", "4", "Buzz"]`

## How I solved it

1. Loop i from 1 to n (`range(1, n + 1)`, so n is included).
2. Check "divisible by both 3 and 5" first. If I checked 3 first, 15 would wrongly become `"Fizz"`.
3. Then check 3, then 5, else append the number as a string.

## Key idea

Order of the checks matters: the most specific case (both) goes first.

## Edge cases

- `n = 1` → `["1"]`.
- 15, 30, 45 must be `"FizzBuzz"`.

## My code

```python
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            if i%3 == 0 and i %5 ==0:
                ans.append("FizzBuzz")
            elif i % 3 ==0:
                ans.append("Fizz")
            elif i %5 ==0:
                ans.append("Buzz")
            else:
                ans.append(f"{i}")

        return ans
```
