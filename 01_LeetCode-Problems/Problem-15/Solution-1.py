"""
3 Sum
"""
class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        for i in range(n-2):
            for j in range(i + 1, n-1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
        return ans
        
sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))

"""
Time Complexity:  O(n³)
Space Complexity: O(1)

"""