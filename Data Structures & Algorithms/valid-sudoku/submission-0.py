class Solution:
    def checkBox(self, board: List[List[str]], a: int, b: int) -> bool:
        s = set()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if board[a+i][b+j] != '.' and board[a+i][b+j] in s:
                    return False
                s.add(board[a+i][b+j])
        return True

    def check(self, board: List[List[str]], a: int, d: int) -> bool:
        s = set()
        for i in range(9):
            if d == 1:
                if board[a][i] != '.' and board[a][i] in s:
                    return False
                s.add(board[a][i])
            if d == -1:
                if board[i][a] != '.' and board[i][a] in s:
                    return False
                s.add(board[i][a])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in [1,4,7]:
            for j in [1,4,7]:
                if not self.checkBox(board, i, j):
                    return False
        for i in range(9):
            if not self.check(board, i, 1):
                return False
        for i in range(9):
            if not self.check(board, i, -1):
                return False
        return True

        
        