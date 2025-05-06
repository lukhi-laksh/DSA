"""
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

"""
class Solution:
    def buildArray(self, nums):

        return [nums[nums[i]] for i in range(len(nums))]

sol = Solution()
nums1 = [0, 2, 1, 5, 3, 4]
nums2 = [5, 0, 1, 2, 3, 4]
print(sol.buildArray(nums1))
print(sol.buildArray(nums2))

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""