class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        while top < bot:
            row = (top + bot + 1) // 2
            if target >= matrix[row][0]:
                top = row
            elif target < matrix[row][0]:
                bot = row-1
        left, right = 0, COLS-1
        while left <= right:
            col = (left + right) // 2
            if target == matrix[top][col]:
                return True
            elif target < matrix[top][col]:
                right = col-1
            else:
                left = col + 1
        return False
