"""
Longest Strictly Increasing or Strictly Decreasing Subarray

"""
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = 1
        dec = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1

            res = max(res, inc, dec)

        return res

"""
Space Complexity: O(n)
Time Complexity: O(1)

"""