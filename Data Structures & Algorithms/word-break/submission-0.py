class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in wordDict:
                if i - len(j) + 1 >= 0 and dp[i+1]==False:
                    # print(i+1, i+1-len(j),  s[i-len(j)+1:i+1], j)
                    dp[i+1] = dp[i+1-len(j)] and (j == s[i-len(j)+1:i+1])
                # print(dp)
        return dp[n]
        