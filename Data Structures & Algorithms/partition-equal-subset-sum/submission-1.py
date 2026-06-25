class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        target = s//2
        if s % 2 == 1:
            return False
        dp = [[False for _ in range(0,target+1)] for _ in range(0,n)]
        for i in range(0, n):
            dp[i][0] = True
        for i in range(0,n):
            for j in range(0,target+1):
                dp[i][j] = dp[i-1][j] 
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]
        return dp[n-1][target]
        