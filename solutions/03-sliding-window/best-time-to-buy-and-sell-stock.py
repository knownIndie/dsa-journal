# Best Time to Buy and Sell Stock · https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Pattern: 03-sliding-window · Difficulty: E
# Time: O(n) · Space: O(1)
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
