"""
Maximum Alternating Sum of Squares

"""
class Solution(object):
    def maxAlternatingSum(self, nums):
        nums = [i**2 for i in nums]
        nums.sort()

        res = sum(nums[len(nums)//2:]) - sum(nums[:len(nums)//2])
        return res

"""
Time Complexity: O(n log n)
Space Complexity: O(n)

"""