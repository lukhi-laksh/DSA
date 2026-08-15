"""
Longest SubSequence with Non Zero Bitwise XOR

"""
class Solution(object):
    def longestSubsequence(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        if xor != 0:
            return len(nums)
        for num in nums:
            if num != 0:
                return len(nums) - 1
        return 0

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""