class Solution:
    def bfs(self, i: int, j: int, grid: List[List[str]], m:int, n:int):
        dir = [[0,1], [0,-1], [-1,0], [1, 0]]
        q = [[i,j]]
        while len(q)!=0:
            a, b = q.pop(0)
            grid[a][b] = '0'
            for k,l in dir:
                if a+k>=0 and a+k<=m-1 and b+l>=0 and b+l<=n-1 and grid[a+k][b+l]=='1':
                    q.append([a+k,b+l])
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    self.bfs(i, j, grid, m, n)
                    cnt += 1

        return cnt
        