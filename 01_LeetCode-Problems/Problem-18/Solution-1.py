"""
4Sum
"""
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = set()
        
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return [list(t) for t in ans]

sol = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(sol.fourSum(nums, target))

"""
Time Complexity:  O(n³)
Space Complexity: O(1)

"""