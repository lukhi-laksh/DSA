"""
Single Number

"""

class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a ^= num

        return a
    
"""
Time Complexity: O(1)
Space Complexity: O(1)

"""