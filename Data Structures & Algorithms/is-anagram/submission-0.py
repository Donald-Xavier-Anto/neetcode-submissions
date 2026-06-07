class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = [0]*26
        freq2 = [0]*26
        for i in s:
            ind = ord(i)-ord('a')
            freq1[ind] += 1
        for i in t:
            ind = ord(i)-ord('a')
            freq2[ind] += 1
        for i in range(0, 26):
            if freq1[i] != freq2[i]:
                return False
        return True
        