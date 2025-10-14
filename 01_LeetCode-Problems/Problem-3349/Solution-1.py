"""
Adjacent Increasing Subarrays Detection I

"""


class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):

        ranges = []
        start = 0
        n = len(nums)

        if k == 1:
            return True

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                ranges.append([start, i])
                start = i

        ranges.append([start, n])

        for i in range(len(ranges)):
            if ranges[i][1] - ranges[i][0] >= 2 * k:
                return True

            if i + 1 < len(ranges) and ranges[i][1] - ranges[i][0] >= k and ranges[i + 1][1] - ranges[i + 1][0] >= k:
                return True

        return False
    

sol = Solution()
print(sol.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3))

"""

Time Complexity:  O(n)
Space Complexity: O(n)

"""