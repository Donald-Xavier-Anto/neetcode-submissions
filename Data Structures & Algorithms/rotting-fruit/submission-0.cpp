class Solution {
    void bfs(vector<vector<int>>& grid, int sx, int sy, vector<vector<int>>& vis) {
        int m = grid.size();
        int n = grid[0].size();
        queue<vector<int>> q;
        q.push({sx, sy, 0});
        vector<vector<int>> dir = {{0,1},{1,0},{-1,0},{0,-1}};
        while (!q.empty()) {
            auto v = q.front();
            q.pop();
            for(int i=0;i<4;i++) {
                int nx = v[0] + dir[i][0];
                int ny = v[1] + dir[i][1];
                if (nx >=0 && ny >= 0 && nx < m && ny < n && grid[nx][ny]==1 && (vis[nx][ny]==-1 || vis[nx][ny]>v[2]+1)) {
                    q.push({nx, ny, v[2]+1});
                    vis[nx][ny] = v[2]+1;
                }
            }
        }
        return;
    }

public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> vis(m, vector<int>(n, -1));
        for (int i=0; i<m; i++) {
            for (int j =0; j<n; j++) {
                if (grid[i][j]==2) {
                    bfs(grid, i, j, vis);
                    vis[i][j] = 0;
                }
            }
        }
        int mx = 0;
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                if (grid[i][j]==1 and vis[i][j]==-1) return -1;
                mx = max(mx, vis[i][j]);
            }
        }
        return mx;
    }
};
