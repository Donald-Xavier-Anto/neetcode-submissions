from queue import PriorityQueue

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = PriorityQueue()
        n = len(nums)
        ans = []
        for i in range(0, n):
            pq.put((-nums[i], i))
            if i >= k-1:
                b=pq.get()
                while  b[1] < (i-k+1):
                    b=pq.get()
                ans.append(-(b[0]))
                pq.put(b)
        return ans
        