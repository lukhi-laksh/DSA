"""
Best Time to Buy and Sell Stock

"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit

sol = Solution()
price = [7, 6, 4, 3, 1]
print(sol.maxProfit(price))

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""