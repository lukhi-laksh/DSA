"""
Elimination Game

"""
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # handle corner case
        if n == 1:
            return 1
        # self.lastRemaining(2k+1) == self.lastRemaining(2k)
        if n % 2 == 1:
            n = n - 1  # now n can be divided by 2
        # self.lastRemaining(2k) = 2 * (k + 1 - self.lastRemaining(k))
        k = n / 2
        return 2 * (k + 1 - self.lastRemaining(k))

"""

Time Complexity: O(log n)
Space Complexity: O(log n)

"""