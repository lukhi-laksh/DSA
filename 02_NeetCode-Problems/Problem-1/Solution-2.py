"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]==nums[j]):
                    return True
        return False

num = [1, 5, 4, 7, 2]
solutions = Solution()
print(solutions.hasDuplicate(num))

"""
Time Complexity: O(n²)
Space Complexity: O(1)

"""