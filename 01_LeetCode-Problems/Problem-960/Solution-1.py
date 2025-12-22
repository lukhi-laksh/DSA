"""
Delete Columns to make Sorted III

"""

class Solution:
    def check(self, v, i, j):
        for k in range(len(v)):
            if v[k][j] > v[k][i]:
                return 0
        return 1

    def minDeletionSize(self, strs):
        dp = [1] * len(strs[0])
        ans = 0
        for i in range(len(strs[0])):
            for j in range(i):
                if self.check(strs, i, j):
                    dp[i] = max(dp[j] + 1, dp[i])
            ans = max(ans, dp[i])
        return len(strs[0]) - ans
    
"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""