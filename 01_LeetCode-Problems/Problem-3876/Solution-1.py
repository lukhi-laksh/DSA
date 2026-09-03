"""
Construct uniform parity Array II

"""

class Solution(object):
    def uniformArray(self, nums1):
        min_val = float('inf')

        for num in nums1:
            if num < min_val:
                min_val = num

        if min_val & 1:
            return True

        for num in nums1:
            if num & 1:
                return False

        return True
"""
Time Complexity: O(n)
Space Complexity: O(1)

"""