class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for k in range(0,n):
            i, j = k, k
            while i>=0 and j<n and s[i]==s[j]:
                cnt += 1
                i -= 1
                j += 1
            i, j = k, k+1
            while i>=0 and j<n and s[i]==s[j]:
                cnt += 1
                i -= 1
                j += 1
        return cnt
            