"""
3sum Closest
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        
        return closest_sum

sol = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(sol.threeSumClosest(nums, target))

"""
Time Complexity:  O(n²)
Space Complexity: O(1)

"""