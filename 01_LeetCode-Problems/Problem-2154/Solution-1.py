"""
Keep Multiplying Found Value by Two

"""

class Solution(object):
    def findFinalValue(self, nums, original):
        s = set(nums)
        print(s)
        while (original in s):
            original *= 2
        return original
    
"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""