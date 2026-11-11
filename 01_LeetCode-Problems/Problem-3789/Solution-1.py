class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        seperate = need1*cost1 + need2*cost2

        both = max(need1,need2)*costBoth

        common = min(need1,need2)*costBoth

        remaining = (
            (need1 - min(need1,need2))* cost1 +
            (need2 - min(need1,need2))* cost2
        )

        mixed = common + remaining
        return min(seperate,both,mixed)

"""
Time Complexity: O(1)
Space Complexity: O(1)

"""