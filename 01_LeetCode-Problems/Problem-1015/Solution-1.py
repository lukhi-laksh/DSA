"""
Smallest Integer Divisible by K

"""

class Solution(object):
    def smallestRepunitDivByK(self, k):
        n = 0
        for i in range(1, k + 1):
            n = n * 10 + 1
            if n % k == 0:
                return i

        return -1

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""