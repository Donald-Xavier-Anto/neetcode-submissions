class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        st = set()
        ans = 0
        for i in range(0, n):
            while s[i] in st:
                st.remove(s[l])
                l += 1
            ans = max(ans, i-l+1)
            st.add(s[i])
        return ans
        