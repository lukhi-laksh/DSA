"""
3 Sum with target = 0
"""
class Solution(object):
    def threeSum(self, nums):
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    temp = (nums[i], nums[left], nums[right])
                    ans.add(temp)
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
       
        return [list(t) for t in ans]

sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))

"""
Time Complexity:  O(n²)
Space Complexity: O(n²)

"""