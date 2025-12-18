"""
Best Time to Buy and Sell Stock using Strategy

"""
class Solution(object):
    def maxProfit(self, prices, strategy, k):
        sm = 0
        for i in range(len(prices)):
            sm += (prices[i] * strategy[i])
        mx = sm
        l = 0
        r = 0
        while r < k:
            if r < k//2:
                sm -= prices[r] * strategy[r]
            else:
                sm -= prices[r] * strategy[r]
                sm += prices[r]
            r +=1 
        
        mx = max(mx,sm)
        while r < len(prices):
            sm += (prices[l] * strategy[l]) + prices[r]
            sm -= prices[r] * strategy[r]
            sm -= (prices[l+(k//2)])
            mx = max(mx,sm)
            l +=1 
            r +=1 
        return mx
    
"""
Time Complexity: O(n)
Space Complexity: O(1)

"""