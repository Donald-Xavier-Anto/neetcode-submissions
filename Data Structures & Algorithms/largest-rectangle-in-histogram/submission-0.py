class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n
        right = [n]*n
        st = []
        for i in range(0, n):
            while len(st)>0 and heights[i]<heights[st[-1]]:
                right[st[-1]] = i
                st.pop()
            st.append(i)
        st.clear()
        for i in range(n-1, -1, -1):
            while len(st)>0 and heights[i]<heights[st[-1]]:
                left[st[-1]] = i
                st.pop()
            st.append(i)
        area = 0
        for i in range(0, n):
            area = max(area, (right[i]-left[i]-1)*heights[i])
        return area
        