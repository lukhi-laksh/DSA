class Solution(object):
    def isValidSudoku(self, board):
        # Create empty list
        # Row check
        empty = list()
        for parent in board:
            empty = list()
            for child in parent:
                if child == ".":
                    continue
                if child in empty:
                    return False
                empty.append(child)
        
        for col in range(9):
            empty = list()
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in empty:
                    return False
                empty.append(cell)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                empty = list()
                for parent in range(3):
                    for child in range(3):
                        cell = board[i + parent][j + child]
                        if cell == ".":
                            continue
                        if cell in empty:
                            return False
                        empty.append(cell)
        return True


sol = Solution()
board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "5", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", "1", ".", "."],
]
print(sol.isValidSudoku(board))
