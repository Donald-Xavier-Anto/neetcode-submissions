class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def build(i, cur, cnt):
            if i==n:
                ans.append(cur[:])
                return
            for j in range(n):
                if nums[j] not in cnt:
                    cnt.add(nums[j])
                    cur.append(nums[j])
                    build(i+1, cur, cnt)
                    cnt.remove(nums[j])
                    cur.pop()
        c = set()
        build(0, [], c)
        return ans
        