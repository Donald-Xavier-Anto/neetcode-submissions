class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        sorted(nums)
        ans = []
        def build(nums, i, target, l, s):
            # print(l, s)
            if s > target:
                return
            if s == target:
                ans.append(l[:])
                return
            if i==n:
                return
            
            
            l.append(nums[i])
            build(nums, i, target, l, s+nums[i])
            l.pop()
            build(nums, i+1, target, l, s)
        build(nums, 0, target, [], 0)
        return ans
            
        