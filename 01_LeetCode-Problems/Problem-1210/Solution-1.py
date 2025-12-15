"""
Number of Smooth Descent Periods of a Stock

"""

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [1] * len(prices)
        res = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1:
                dp[i] = dp[i-1] + 1
                res = res + dp[i]
            else:
                dp[i] = 1
                res = res + dp[i]
        print(res)
        return res

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""