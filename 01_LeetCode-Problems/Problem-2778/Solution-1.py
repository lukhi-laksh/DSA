"""
Sum of Squares of Special Elements

"""
class Solution(object):
    def sumOfSquares(self, nums):

        n = len(nums)
        total = 0

        for i in range(1, n + 1):
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]

        return total

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""