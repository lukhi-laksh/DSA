"""
Largest Perimeter Triangle

"""
class Solution(object):
    def largestPerimeter(self, nums):
        if len(nums) < 3: return 0
        nums.sort(reverse=True)
        a, b = nums[:2]
        for c in nums[2:]:
            if b + c > a:
                return a + b + c
            a, b = b, c
        return 0

sol = Solution()
print(sol.largestPerimeter([2, 1, 2]))

"""
Time Complexity:  O(n log n)
Space Complexity: O(n)

"""