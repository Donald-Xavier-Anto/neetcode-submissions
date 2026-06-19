class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def build(i, cnt, l):
            if cnt < 0 or cnt > n:
                return
            if i==n:
                if cnt == 0:
                    ans.append("".join(l))
                elif cnt > 0:
                    r = l.copy()
                    while cnt != 0:
                        r.append(")")
                        cnt -= 1
                    ans.append("".join(r))
                return
            l.append("(")
            build(i+1, cnt+1, l)
            l.pop()
            l.append(")")
            build(i, cnt-1, l)
            l.pop()
        build(0, 0, [])
        return ans
