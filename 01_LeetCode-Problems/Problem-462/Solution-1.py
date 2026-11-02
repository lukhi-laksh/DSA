"""
Minimum Moves to Equal Array Elements II

"""
class Solution(object):
    def minMoves2(self, nums):
        c=0
        nums.sort()
        n=len(nums)
        m=nums[n//2]

        for num in nums:
            c += abs(num - m)

        return c

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""