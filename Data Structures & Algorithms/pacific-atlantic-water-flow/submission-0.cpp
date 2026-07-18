class Solution {
    void bfs(vector<vector<int>>& h, queue<vector<int>>& q, vector<vector<bool>>& vis) {
        int m = h.size(), n = h[0].size();
        int dir[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
        while(!q.empty()) {
            vector<int> cur = q.front();
            q.pop();
            for(int i=0;i<4;i++) {
                int x = cur[0] + dir[i][0], y = cur[1] + dir[i][1];
                if (x<m && x>=0 && y<n && y>=0 && !vis[x][y] && h[x][y]>=h[cur[0]][cur[1]]) {
                    q.push({x,y});
                    vis[x][y] = true;
                }
            }
        }
        return;
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        queue<vector<int>> q;
        int m = heights.size(), n = heights[0].size();
        vector<vector<int>> ans;
        vector<vector<bool>> visp(m, vector<bool>(n, false));
        vector<vector<bool>> visa(m, vector<bool>(n, false));
        for(int j=0;j<n;j++) {
            q.push({0,j});
            visp[0][j] = true;
        }
        for(int i=0;i<m;i++) {
            q.push({i,0});
            visp[i][0] = true;
        }
        bfs(heights, q, visp);
        for(int j=0;j<n;j++) {
            q.push({m-1,j});
            visa[m-1][j] = true;
        }
        for(int i=0;i<m;i++) {
            q.push({i,n-1});
            visa[i][n-1] = true;
        }
        bfs(heights, q, visa);
        for (int i=0;i<m;i++) { 
            for (int j=0;j<n;j++) {
                if (visa[i][j] && visp[i][j]) ans.push_back({i,j});
            }
        }
        return ans;
    }
};
