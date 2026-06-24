class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one, two = 1, 1
        ans = 0
        for i in range(2,n+1):
            ans = one + two
            one, two = ans, one
        return ans
        