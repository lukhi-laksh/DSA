"""
Check if number is a sum of powers of Three

"""

from math import floor, log

class Solution(object):
    def checkPowersOfThree(self, n, power=-2):

        if n == 0:
            return True
        if power == -1:
            return False
        if power == -2:
            power = floor(log(n, 3))
        return self.checkPowersOfThree(n - 3 ** power, power - 1) or self.checkPowersOfThree(n, power - 1)

"""
Time Complexity: O(2^log n)
Space Complexity: O(log n)

"""
        