class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        def build(target, l, s, i):
            if s==target:
                ans.append(l[:])
                return
            if s>target or i>=n:
                return
            j = i
            while j+1<n and nums[j]==nums[j+1]:
                j += 1
            for k in range(i, j+1):
                l.append(nums[i])
                build(target, l, s+((k-i+1)*nums[i]), j+1)
            for _ in range(i, j+1):
                l.pop()
            build(target, l, s, j+1)
        build(target, [], 0, 0)
        return ans 
            