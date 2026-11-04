# Best Time to Buy and Sell Stock

[LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · Pattern: 03-sliding-window · Difficulty: E  
Time: O(n) · Space: O(1)

## Question

You get `prices`, where `prices[i]` is a stock's price on day i. Buy on one day and sell on a later day. Return the biggest profit you can make, or 0 if no profit is possible.

Example: `[7, 1, 5, 3, 6, 4]` → `5` (buy at 1, sell at 6)

## How I solved it

1. Keep `lowest`: the cheapest price seen so far. Start it at `prices[0]`.
2. Keep `bestbuy`: the best profit so far. Start it at 0.
3. Walk the prices from day 1. For each price, profit if I sell today = `price - lowest`. If that beats `bestbuy`, update it.
4. Then update `lowest = min(lowest, price)`, so later days can buy at this price.
5. Return `bestbuy`.

## Key idea

For each sell day, the best buy day is the cheapest day **before** it. So track the running minimum and the best `price - minimum`. One pass, O(1) space.

## Edge cases

- Prices only go down (`[7, 6, 4, 3, 1]`) → 0.
- One day → 0 (you can't buy and sell).

## My code

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest=prices[0]
        bestbuy=0
        for i in prices[1:]:
            diff=i-lowest
            if i>lowest:
                bestbuy = max(bestbuy,diff )
            lowest = min(lowest , i)
        return bestbuy
```
