class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        grid = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    if board[r][c] in row[r]:
                        return False

                    if board[r][c] in col[c]:
                        return False

                    if board[r][c] in grid[r // 3, c // 3]:
                        return False
                    
                    row[r].append(board[r][c])
                    col[c].append(board[r][c])
                    grid[r // 3, c // 3].append(board[r][c])

        return True