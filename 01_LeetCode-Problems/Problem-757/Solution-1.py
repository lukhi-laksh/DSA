"""
Set Intersection Size At Least Two

"""

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        need = [2] * n
        res = 0
        while n:
            s, e = intervals[n-1]
            k = need[n-1]
            n -= 1
            for x in range(s, s + k):
                for i in range(n):
                    if need[i] and x <= intervals[i][1]:
                        need[i] -= 1
                res += 1
        return res

    

"""
Time Complexity:  O(n²)
Space Complexity: O(n)

"""

