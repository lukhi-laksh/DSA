"""
Maximum Total Damage With Spell Casting

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
            include = total[i]
            j = bisect_right(nums, nums[i] - 3) - 1
            if j >= 0:
                include += dp[j]
            
            exclude = dp[i-1] if i > 0 else 0
            
            dp[i] = max(include, exclude)
        
        return dp[-1]
    

"""

Time Complexity:  O(n)
Space Complexity: O(n)

"""