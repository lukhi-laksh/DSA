"""
Remove Duplicate From Sorted Array II

"""

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        left, mid, right = 0,1,2

        while right <= len(nums):
            if nums[left]==nums[mid]==nums[right]:
                nums.remove(nums[right])
            else:
                left += 1
                mid += 1
                right += 1
            if right >= len(nums):
                    break
        

        return len(nums)

"""
Time Complexity: O(n²)
Space Complexity: O(1)

"""