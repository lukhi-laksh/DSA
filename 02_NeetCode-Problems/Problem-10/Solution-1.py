class Solution(object):
    def MaxOfMin(self, board):
        ans = [0] * len(board)
        for i in range(len(board)):
            for j in range(len(board) - i):
                check = 2**31 - 1
                for k in range(j, j + i + 1):
                    check = min(check, board[k])
                ans[i] = max(ans[i], check)    
        return ans
