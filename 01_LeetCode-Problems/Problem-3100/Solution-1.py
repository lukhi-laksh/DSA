class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        filled_bottels = numBottles
        empty_botels = 0
        total_bottels = numBottles
        count = 0
        while(total_bottels>=numExchange):
            count = filled_bottels + count
            filled_bottels = 1
            empty_botels = total_bottels - numExchange
            total_bottels = filled_bottels + empty_botels
            numExchange = numExchange +1
            # print(count,filled_bottels,empty_botels,total_bottels)
        return count  + filled_bottels
    

sol = Solution()
print(sol.maxBottlesDrunk(20, 3))
        