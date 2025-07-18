from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row(board):
            for parent in board:
                final = set()
                for child in parent:
                    if child == ".":
                        continue
                    if child in final:
                        print("congraulation error accurs")
                        return False
                    final.add(child)
            return True
        
        
        def columns(board: List[List[str]]) -> bool:
            for col in range(9):
                final = set()
                for row in range(9):
                    cell = board[row][col]
                    if cell == '.':
                        continue
                    if cell in final:
                        return False
                    final.add(cell)
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
    [".", ".", ".", ".", "8", ".", ".", ".", "9"],
]
print(sol.isValidSudoku(board))
