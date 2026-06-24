class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        o = set()
        ans = []
        def solve(i):
            nonlocal ans
            if i == n:
                ans.append(board[:])
                return
            for j in range(0,n):
                if (j not in o) and ((str(i+j)+"x") not in o) and ((str(i-j)+"y") not in o):
                    o.add(j)
                    o.add((str(i+j)+"x"))
                    o.add((str(i-j)+"y"))
                    board.append(j)
                    solve(i+1)
                    board.pop()
                    o.remove(j)
                    o.remove((str(i+j)+"x"))
                    o.remove((str(i-j)+"y"))
            return
        solve(0)
        a = []
        for j in range(0, len(ans)):
            row = 0
            b = [["." for i in range(0,n)] for _ in range(0,n)]
            for i in ans[j]:
                b[row][i] = 'Q'
                b[row] = "".join(b[row])
                row += 1
            a.append(b[:])
        return a