class Solution(object):
    def MaxOfMin(self, board):
        # Create array of 0 value
        ans = [0] * len(board)
        # Outer Loop
        for i in range(len(board)):
            for j in range(len(board) - i):
                check = 2**31 - 1
                for k in range(j, j + i + 1):
                    check = min(check, board[k])
                ans[i] = max(ans[i], check)    
        return ans

sol = Solution()
board = [10, 20, 15, 50, 10, 70, 30]
print(sol.MaxOfMin(board))
