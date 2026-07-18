class Solution {
    void bfs(vector<vector<char>>& b, queue<vector<int>>& q, vector<vector<bool>>& vis) {
        int m = b.size(), n = b[0].size();
        int dir[4][2] = {{0,1},{1,0},{-1,0},{0,-1}};
        while(!q.empty()) {
            vector<int> cur = q.front();
            q.pop();
            for(int i=0;i<4;i++) {
                int x = cur[0] + dir[i][0], y = cur[1] + dir[i][1];
                if (x<m && x>=0 && y<n && y>=0 && !vis[x][y] && b[x][y]=='O') {
                    q.push({x,y});
                    vis[x][y] = true;
                }
            }
        }
        return;
    }
public:
    void solve(vector<vector<char>>& board) {
        queue<vector<int>> q;
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        for(int j=0;j<n;j++) {
            if (board[0][j]=='O') {
                q.push({0,j});
                vis[0][j] = true;
            }
        }
        for(int i=1;i<m;i++) {
            if (board[i][0]=='O') {
                q.push({i,0});
                vis[i][0] = true;
            }
        }
        for(int j=1;j<n;j++) {
            if (board[m-1][j]=='O') {
                q.push({m-1,j});
                vis[m-1][j] = true;
            }
        }
        for(int i=1;i<m-1;i++) {
            if (board[i][n-1]=='O') {
                q.push({i,n-1});
                vis[i][n-1] = true;
            }
        }
        bfs(board, q, vis);
        for (int i=0;i<m;i++) { 
            for (int j=0;j<n;j++) {
                if (!vis[i][j] && board[i][j]=='O') board[i][j] = 'X';
            }
        }
        return;
    }
};
