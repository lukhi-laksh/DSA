"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

class Solution(object):
    def containsDuplicate(self, nums):
        new_nums = sorted(nums)

        for i in range(1, len(nums)-1):
                if (new_nums[i] == new_nums[i+1]):
                    return True
        return False
            
    
sol = Solution()
nums = [2, 3, 4, 6, 3]
print(sol.containsDuplicate(nums))

"""
Time Complexity: O(n log n)
Space Complexity: O(n)

"""