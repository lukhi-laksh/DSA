"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

"""
class Solution(object):
    def firstMissingPositive(self, nums):
        nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums:
                return i
        return len(nums) + 1

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""