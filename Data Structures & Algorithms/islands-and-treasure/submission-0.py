class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        vis = [[-1 for _ in range(n)] for _ in range(m)]
        dir = [(0,1), (1,0), (-1,0), (0,-1)]
        def bfs(sx, sy, dis):
            queue = deque()
            queue.append((sx, sy, dis))
            while len(queue) != 0:
                x, y, z = queue.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny]!=-1 and grid[nx][ny]!=0 and z+1<grid[nx][ny]:
                        vis[nx][ny] = 0
                        grid[nx][ny] = z + 1
                        queue.append((nx, ny, z + 1))
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i, j, 0)
        return 

        