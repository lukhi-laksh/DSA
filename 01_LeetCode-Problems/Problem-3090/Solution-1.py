"""
Maximum Length Substring With Two Occurrences

"""
class Solution:
    def maximumLengthSubstring(self, s):
        n = len(s)
        res = 0
        f = [0] * 26

        l = 0
        for r in range(n):
            f[ord(s[r]) - ord('a')] += 1

            while f[ord(s[r]) - ord('a')] > 2:
                f[ord(s[l]) - ord('a')] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

"""

Time Complexity: O(n)
Space Complexity: O(1)

"""