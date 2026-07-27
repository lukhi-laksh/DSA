"""
Maximum Product of Two Eliments in Array

"""
class Solution(object):
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        return (nums[0]-1)*(nums[1]-1)

"""
Time Complexity:  O(1)
Space Complexity: O(1)

"""