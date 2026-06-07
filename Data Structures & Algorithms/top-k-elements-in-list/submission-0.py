class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        return [key for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)][0:k]
        