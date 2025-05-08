"""
Best Time to Buy and Sell Stock

"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                check = prices[j] - prices[i]
                if check > max_profit:
                    max_profit = check
        return max_profit
sol = Solution()
price = [7, 6, 4, 3, 1]
print(sol.maxProfit(price))

"""
Time Complexity: O(n²)
Space Complexity: O(1)

"""