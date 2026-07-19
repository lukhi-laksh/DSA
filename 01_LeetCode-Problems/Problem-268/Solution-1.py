"""
Missing Number

"""

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""
