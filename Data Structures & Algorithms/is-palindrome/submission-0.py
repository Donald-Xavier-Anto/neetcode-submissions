class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = [i for i in s if i.isalnum()]
        return all([(s[i] == s[len(s)-1-i]) for i in range(0, len(s)//2)])
        