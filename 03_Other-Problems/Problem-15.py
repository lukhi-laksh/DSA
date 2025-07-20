from typing import List

# main class
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
        
        # Check columns
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
        
        # Row check
        def box(board: List[List[str]]) -> bool:
            for col in range(0, 9, 3):
                for row in range(0, 9, 3):
                    final = set()
                    for i in range(3):
                        for j in range(3):
                            temp = board[row + i][col + j]
                            if temp == '.':
                                continue
                            if temp in final:
                                return False
                            final.add(temp)
            return True

                        
        
        return row(board) and columns(board) and box(board)
        

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
