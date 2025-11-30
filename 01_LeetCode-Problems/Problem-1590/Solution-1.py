"""
Make Array divisible by P

"""

from collections import defaultdict


class Solution(object):
    def minSubarray(self, nums, p):
        n = len(nums)
        mod = sum(nums) % p
        if mod == 0: return 0
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0] % p
        index_map = defaultdict(int)
        index_map[prefix_sum[0]] = 1
        count = n
        for i in range(n):
            if i > 0:
                prefix_sum[i] += (prefix_sum[i-1] + nums[i]) % p
            if prefix_sum[i] % p == 0:
                count = min(n - i - 1, count)
            if prefix_sum[i] % p == mod:
                count = min(i + 1, count)
            if index_map[(p - mod + prefix_sum[i]) % p] > 0:
                count = min(i + 1 - index_map[(p - mod + prefix_sum[i]) % p], count)
            index_map[prefix_sum[i]] = i + 1
        return count if count < n else -1

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""