class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for i in strs:
            res += str(len(i)) + "|" + i
        return res
        
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        i, j = 0, 0
        ans = []
        t = ""
        while j!=len(s):
            if s[i] != "|":
                t += s[i]
                i += 1
            elif s[i] == "|":
                i += 1
                j = i + int(t)
                t = ""
                ans.append(s[i:j])
                i = j
        return ans
            

