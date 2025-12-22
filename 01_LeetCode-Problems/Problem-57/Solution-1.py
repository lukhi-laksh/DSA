"""
Insert Interval

"""

class Solution(object):
    def insert(self, intervals, newInterval):

        result = []
        new = newInterval[:]
        for interval in intervals:
            if interval[0] > newInterval[1]:
                if new:
                    result.append(new)
                    new = None
                result.append(interval[:])
            elif interval[1] < newInterval[0]:
                result.append(interval[:])
            else:
                new[0] = min(new[0], interval[0])
                new[1] = max(new[1], interval[1])
        if new:
            result.append(new)
        return result

"""
Time Complexity: O(n)
Space Complexity: O(n)

"""