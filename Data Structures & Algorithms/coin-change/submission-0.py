class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i] = min(dp[i], dp[i-j]+1)
            # print(i, dp)
        return dp[amount] if dp[amount]!=100000 else -1
        