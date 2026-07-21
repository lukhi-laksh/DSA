"""
Square of a Sorted Array

"""
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        
        l, r = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            
            if left > right:
                res[i] = left
                l += 1
            else:
                res[i] = right
                r -= 1
        
        return res

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""