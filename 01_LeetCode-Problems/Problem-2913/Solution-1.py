"""
Subarrays Distinct Element Sum of Squares I

"""
class Solution(object):
    def sumCounts(self, nums):
        res = 0

        for i in range(len(nums)):
            s = set()

            for j in range(i, len(nums)):
                s.add(nums[j])
                res += len(s) ** 2

        return res

"""
Time Complexity: O(n²)
Space Complexity: O(n)

"""