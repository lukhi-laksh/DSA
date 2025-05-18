class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if nums[i] == i:
                return i
        return -1

sol = Solution()
nums = []
print(sol.smallestIndex(nums))