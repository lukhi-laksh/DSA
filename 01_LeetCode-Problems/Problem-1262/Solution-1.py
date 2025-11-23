"""
Greatest Sum Divisible by Three

"""

class Solution(object):
    def maxSumDivThree(self, nums):

        n = len(nums)
        NEGA_INF = -10**9
        dp = {}

        def maxSumAt(i, remainder):
            if i == n:
                if remainder == 0:
                    return 0
                return NEGA_INF

            key = (i, remainder)
            if key in dp:
                return dp[key]

            skip = maxSumAt(i + 1, remainder)

            newRemain = (remainder + nums[i]) % 3

            take = nums[i] + maxSumAt(i + 1, newRemain)

            dp[key] = max(skip, take)
            return dp[key]
        
        return maxSumAt(0, 0)
    

"""
Time Complexity:  O(n)
Space Complexity: O(n)

"""