class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }
        ans = []
        l = []
        def solve(i):
            if i == len(digits):
                print(l)
                ans.append("".join(l))
                return
            # print(d[int(digits[i])])
            for j in d[int(digits[i])]:
                l.append(j)
                solve(i+1)
                l.pop()
            return
        solve(0)
        return ans