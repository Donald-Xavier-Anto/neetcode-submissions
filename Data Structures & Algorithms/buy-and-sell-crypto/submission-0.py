class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        profit = 0
        for i in prices[::-1]:
            profit = max(profit, mx - i)
            mx = max(mx, i)
        return profit
        