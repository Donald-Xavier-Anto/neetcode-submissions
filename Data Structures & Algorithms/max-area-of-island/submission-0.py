class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        vis = [[-1 for _ in range(n)] for _ in range(m)]
        dir = [(0,1),(0,-1),(-1,0),(1,0)]
        def bfs(sx, sy, id):
            queue = deque()
            queue.append((sx,sy,id))
            while len(queue)!=0:
                x, y, z = queue.popleft()
                for (dx, dy) in dir:
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < m and ny >=0 and ny < n and grid[nx][ny]==1 and vis[nx][ny]==-1:
                        vis[nx][ny] = z
                        queue.append((nx, ny, z))
            return
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == -1:
                    vis[i][j] = cnt
                    bfs(i, j, cnt)
                    cnt += 1
                    
        counts = dict(Counter(item for row in vis for item in row))
        mx = 0
        for i, v in counts.items():
            if i != -1:
                mx = max(mx, v)
        return mx
                    



        