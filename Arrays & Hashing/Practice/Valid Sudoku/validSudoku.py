class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, square = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in square[row//3, col//3]:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[row//3, col//3].add(board[row][col])

        
        return True