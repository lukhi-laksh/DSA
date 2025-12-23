"""
Two Best Non-Overlapping Events

"""

import heapq

class Solution(object):
    def maxTwoEvents(self, events):
        events.sort(key=lambda x: x[0])
        ans = 0
        preMax = 0
        q = []
        for i, e in enumerate(events):
            while q and q[0][0] < e[0]:
                preMax = max(preMax, heapq.heappop(q)[1])
            ans = max(ans, e[2] + preMax)
            heapq.heappush(q, [e[1], e[2]])
        return ans
    
"""
Time Complexity: O(n log n)
Space Complexity: O(n)

"""

        