class Solution:
    def buildArray(self, nums):

        return [nums[nums[i]] for i in range(len(nums))]

sol = Solution()
nums1 = [0, 2, 1, 5, 3, 4]
nums2 = [5, 0, 1, 2, 3, 4]
print(sol.buildArray(nums1))
print(sol.buildArray(nums2))
