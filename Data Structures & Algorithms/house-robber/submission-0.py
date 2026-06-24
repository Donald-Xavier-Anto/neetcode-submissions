class Solution:
    def rob(self, nums: List[int]) -> int:
        mx, pre = 0, nums[0]
        for i in range(1, len(nums)):
            temp = max(mx + nums[i], pre)
            mx, pre = pre, temp
        return pre
        