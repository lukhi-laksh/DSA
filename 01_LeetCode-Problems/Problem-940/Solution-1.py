"""
Distinct Subseqences II

"""
class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007

        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            total = 1
            for x in dp:
                total = (total + x) % MOD

            dp[i] = total

        return sum(dp) % MOD
"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""