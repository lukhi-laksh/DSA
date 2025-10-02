"""
Water Bottles

"""

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        
        ans = numBottles
        
        while numBottles >= numExchange:
            ans += numBottles // numExchange
            left = numBottles % numExchange
            
            numBottles = numBottles // numExchange + left
            
        return ans

sol = Solution()
print(sol.numWaterBottles(15, 3))

