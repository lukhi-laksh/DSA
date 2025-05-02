"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

"""
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i -1]:
                return True
        return False
    
num = [7, 1, 5, 4, 7, 2]
solutions = Solution()
print(solutions.hasDuplicate(num))

"""
Time Complexity: O(n log n)
Space Complexity: O(1)

"""