class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(0, n)] for _ in range(0, n)]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
            if i+1<n and s[i]==s[i+1]:
                dp[i][i+1] = True
                ans = s[i:i+2]
        for l in range(3, n+1):
            for i in range(0, n):
                if i+l-1 < n:
                    dp[i][i+l-1] = dp[i+1][i+l-2] and (s[i] == s[i+l-1])
                    if dp[i][i+l-1]:
                        # print(i,i+l)
                        ans = s[i:i+l]
        # print(dp)
        return ans
        