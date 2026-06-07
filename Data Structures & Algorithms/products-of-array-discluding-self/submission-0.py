class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        suf = [1]*(len(nums))
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1]*nums[i+1]
        pre = 1
        for i in range(len(nums)):
            ans.append(suf[i]*pre)
            pre *= nums[i]
        return ans;


        