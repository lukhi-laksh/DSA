"""
Find the Lexicographically Smallest Valid Sequence

"""

class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            if dp[i + 1] < m:
                k = m - dp[i + 1] - 1

                if word1[i] == word2[k]:
                    dp[i] += 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not changed:
                if dp[i + 1] >= m - j - 1:
                    ans.append(i)
                    j += 1
                    changed = True

        if j == m:
            return ans

        return []

"""

Time Complexity:  O(n)
Space Complexity: O(n)

"""