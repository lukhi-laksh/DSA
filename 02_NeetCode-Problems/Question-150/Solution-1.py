"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

num = [1, 2, 5, 4, 7, 2]
solutions = Solution()
print(solutions.hasDuplicate(num))

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""