"""
Minimum Number of Pushes to Type Word II

"""

class Solution(object):
    def minimumPushes(self, word):
        nums = sorted(Counter(word).values(), reverse = True)
        return sum(nums[: 8]) + 2 * sum(nums[8 : 16]) + sum(nums[16 : 24]) * 3 + sum(nums[24 : ]) * 4

"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""