class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        nums = sorted(nums)
        ans = 0
        for i in nums:
            d[i] = d[i-1]+1
            ans = max(ans, d[i])
        return ans
        