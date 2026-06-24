class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def check(sr):
            return sr == sr[::-1]

        def solve(l, pre):
            if pre==len(s):
                ans.append(l[:])
                return 
            
            for j in range(pre, len(s)):
                if check(s[pre:j+1]):
                    l.append(s[pre:j+1])
                    solve(l, j+1)
                    l.pop()

            return 
        solve([], 0)
        return ans
        