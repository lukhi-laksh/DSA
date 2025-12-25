"""
Maximize Happiness of Selected Children 

"""


class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        
        happiness.sort(reverse = True)

        protected = []
        for i in range(k):
            top = happiness[0]
            happiness.remove(top)
            if top - i > 0:
                protected.append(top - i)

        return sum(protected)

"""
Time Complexity: O(n log n + n·k)
Space Complexity: O(k)

"""