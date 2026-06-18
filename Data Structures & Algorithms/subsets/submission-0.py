class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sorted(nums)
        ans = []
        def subset_build(nums, i, s):
            if i == len(nums):
                print(s)
                ans.append(s[:])
                return
    
            s.append(nums[i])
            subset_build(nums, i+1, s)
            s.pop() 
            subset_build(nums, i+1, s)
                  
        subset_build(nums, 0, [])
        return ans   