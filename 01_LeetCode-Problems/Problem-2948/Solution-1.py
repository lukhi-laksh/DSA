"""
Make Lexicographically Smallest Array by Swapping Elements

"""
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = sorted((nums[i], i) for i in range(n))
        ans = nums[:]
        start = 0
        while start < n:
            end = start
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1
            indices = sorted(arr[i][1] for i in range(start, end + 1))
            values = [arr[i][0] for i in range(start, end + 1)]

            for i in range(len(indices)):
                ans[indices[i]] = values[i]
            start = end + 1
        return ans

"""

Time Complexity:  O(n log n)
Space Complexity: O(n)

"""