"""
Maximum Total Damage With spell casting

"""

from bisect import bisect_right
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        freq = Counter(power)
        nums = sorted(freq.keys())
        total = [num * freq[num] for num in nums]
        
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            # profit if we take current spell group
            include = total[i]
            # find last non-conflicting spell (nums[j] < nums[i] - 2)
            j = bisect_right(nums, nums[i] - 3) - 1
            if j >= 0:
                include += dp[j]
            
            # profit if we skip this one
            exclude = dp[i-1] if i > 0 else 0
            
            dp[i] = max(include, exclude)
        
        return dp[-1]
    

