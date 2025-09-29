"""
Ugly Number
"""
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        return n == 1


sol = Solution()
print(sol.isUgly(14))

"""
Time Complexity:  O(log n)
Space Complexity: O(1)
"""
