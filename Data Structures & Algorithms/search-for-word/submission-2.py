class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        queue = deque()
        m, n = len(board), len(board[0])
        if len(word) > m*n:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    queue.append((i, j, 0, (-2,-2)))
        # print(queue
        while len(queue)!=0:
            i, j, k, d = queue.popleft()
            if k == len(word)-1:
                return True
            for x,y in dir:
                if i+x >= 0 and i+x < m and j+y >= 0 and j+y < n and (i+x,j+y)!=d and word[k+1]==board[i+x][j+y]:
                    queue.append((i+x, j+y, k+1, (i,j)))
            # print(queue)
        return False


        