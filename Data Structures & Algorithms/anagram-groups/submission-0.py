class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in strs:
            t = str(sorted(i))
            if t in words:
                words[t].append(i)
            else:
                words[t] = [i]
        ans = []
        for k,v in words.items():
            ans.append(v)
        return ans

        