"""
Count Nice Pairs in an Array

"""

from typing import Counter

class Solution(object):
    def countNicePairs(self, nums):
        d = Counter([num - int(str(num)[::-1]) for num in nums]).values()
        return sum([num * (num - 1) // 2 for num in d]) % (10 ** 9 + 7)

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""