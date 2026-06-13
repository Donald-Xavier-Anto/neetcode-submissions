class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lk , rk = 1, 1000000000
        def check(m, h):
            total = 0
            for i in piles:
                total += (i+m-1)//m
            return total <= h 
        while lk < rk:
            mk = (lk + rk)//2
            if check(mk, h):
                rk = mk
            else:
                lk = mk + 1
        return rk
        