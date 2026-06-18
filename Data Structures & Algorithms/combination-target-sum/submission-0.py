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
            
            cnt = 1 + ((target-nums[i])//nums[i])
            for j in range(1,cnt+1):
                l.append(nums[i])
                build(nums, i+1, target, l, s+(j*nums[i]))
            for _ in range(1, cnt+1):
                l.pop()
            build(nums, i+1, target, l, s)
        build(nums, 0, target, [], 0)
        return ans
            
        