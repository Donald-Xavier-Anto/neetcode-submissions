class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        def build(i, cur):
            if i == n:
                ans.append(cur[:])
                return 

            cur.append(nums[i])
            build(i+1, cur)
            cur.pop()
            j = i
            while j+1<n and nums[j]==nums[j+1]:
                j += 1
            build(j+1, cur)
        build(0, [])
        return ans

        