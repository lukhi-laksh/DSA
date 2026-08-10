"""
Stone Game VI

"""
class Solution:
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)

        for i in range(n + 1):
            if not dp[i]:
                j = 1

                while i + j * j <= n:
                    dp[i + j * j] = True
                    j += 1

                if dp[n]:
                    return True

        return False

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""