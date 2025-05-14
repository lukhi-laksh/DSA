"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

"""
class Solution(object):
    def firstMissingPositive(self, nums):
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i
sol = Solution()
nums = [2, 3, -7, 3, 1, 4]
print(sol.firstMissingPositive(nums))  

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""