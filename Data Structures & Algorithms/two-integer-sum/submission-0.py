class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            print(seen)
            if seen.get(target - nums[i], -1) != -1:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i
        return [] 
        