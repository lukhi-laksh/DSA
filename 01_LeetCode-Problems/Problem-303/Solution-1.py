"""
Range Sum Query - Immutable

"""

class NumArray(object):
    def __init__(self, nums):
        self.arr=nums

    def sumRange(self, left, right):
        return(sum(self.arr[left:right+1]))
    
"""
Time Complexity:  O(1)
Space Complexity: O(1)

"""