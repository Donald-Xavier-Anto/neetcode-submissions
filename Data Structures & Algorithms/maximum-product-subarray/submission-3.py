class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg = []
        zeroes = {}
        mn = -float("infinity")
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(i)
                mn = max(mn, nums[i])
            if nums[i] == 0:
                zeroes[i] = neg[:]
                neg = []
                mn = 0
        zeroes[len(nums)] = neg
        print(zeroes)
        def solve(i, j):
            if i == j:
                return 0
            if len(zeroes[j])%2 == 0:
                return math.prod(nums[i:j])
            return max(math.prod(nums[i:zeroes[j][-1]]), math.prod(nums[zeroes[j][0]+1:j]))
        
        prev = 0
        mx = -float("infinity")
        for i,_ in zeroes.items():
            if i-prev==1 and nums[prev]<0:
                mx = max(mx, nums[prev])
            else:
                mx = max(mx, solve(prev, i))
            prev = i+1 
        return max(mx, mn)