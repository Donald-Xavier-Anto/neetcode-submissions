class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mx, pre = 0, nums[0]
        for i in range(1, len(nums)-1):
            temp = max(mx + nums[i], pre)
            mx, pre = pre, temp
        ans = pre
        mx, pre = 0, nums[1]
        for i in range(2, len(nums)):
            temp = max(mx + nums[i], pre)
            mx, pre = pre, temp
        return max(ans,pre)
        