class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        st = []
        ans = [0]*n
        for i, val in enumerate(t):
            while len(st)>0 and val>t[st[-1]]:
                ans[st[-1]] = i-st[-1]
                st.pop()
            st.append(i)
        return ans
