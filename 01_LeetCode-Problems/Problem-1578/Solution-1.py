"""
Minimum Time to Make Rope Colorful

"""
class Solution(object):
    def minCost(self, colors, neededTime):
        n = len(colors)
        ans = 0
        group_color = ''
        total_time = 0
        max_time = 0

        for i in range(n):
            if colors[i] == group_color:
                total_time += neededTime[i]
                max_time = max(max_time, neededTime[i])
            else:
                ans += total_time - max_time
                group_color = colors[i]
                total_time = neededTime[i]
                max_time = neededTime[i]

        ans += total_time - max_time
        return ans
    
"""
Time Complexity:  O(n)
Space Complexity: O(1)

"""