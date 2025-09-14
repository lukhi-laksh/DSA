class Solution(object):
    def countSubarrays(self, nums, k):
        left = right = 0
        windowSum = 0
        valid = 0
        while right < len(nums):
            windowSum += nums[right]
            right += 1
            
            while left < right and windowSum * (right - left) >= k:
                windowSum -= nums[left] 
                left += 1
            
            valid += right - left
        
        return valid
        