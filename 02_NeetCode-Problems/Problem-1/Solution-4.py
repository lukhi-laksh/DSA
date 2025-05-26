"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

"""
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = list()
        for i in nums:
            if i in empty:
                return True
            else:
                empty.append(i)
        return False

sol = Solution()
nums = [2, 3, 4, 4, 2]
print(sol.hasDuplicate(nums))

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""