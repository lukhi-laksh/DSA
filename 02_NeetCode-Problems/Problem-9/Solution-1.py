from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for val in board:
            if val == ".":
                continue
            if val in seen:
                print("congraulation error accurs")
                break
        seen[val] = True
        return seen  



sol = Solution()
board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", ".", "9"],   
]
print(sol.isValidSudoku(board))
