"""
Maximize Sum of Squares of Digits

"""
class Solution:
    def maxSumOfSquares(self, num, s):
        if s == 0:
            return "0" if num == 1 else ""
        if s > 9*num or s < 1:
            return ""
        ans = ""
        for i in range(num):
            d = 9 if s >= 9 else s
            ans += str(d)
            s -= d
        return ans
"""
Time Complexity: O(n²)
Space Complexity: O(n)

"""