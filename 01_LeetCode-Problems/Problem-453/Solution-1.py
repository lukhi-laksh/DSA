class Solution(object):
    def minMoves(self, nums):
        n = len(nums)
        s = sum(nums)
        m = min(nums)

        return s - n * m