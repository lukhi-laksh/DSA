"""
Adjacent Increasing Subarrays Detection II

"""

class Solution(object):
    def maxIncreasingSubarrays(self, nums):

        if len(nums) <= 1:
            return 1
        
        l = 0  # Last/previous sequence length
        c = 1  # Current sequence length
        m = 0  # Maximum k found
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                m = max(m, max(c//2, min(c, l)))
                l = c
                c = 1
        
        m = max(m, max(c//2, min(c, l)))
        return m

sol = Solution()
print(sol.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))

"""

Time Complexity:  O(n)
Space Complexity: O(1)

"""